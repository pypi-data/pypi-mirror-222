#include "caseo.h"

#include <stdio.h>
#include <math.h>

#include "cutils.h"
#include "ctree.h"
#include "cmodel.h"
#include "cdata.h"

bool watch_minimize(clingo_weight_t p, const clingo_weighted_literal_t *W, size_t n, void *data) {
  void **pack = (void**) data;
  clingo_weighted_literal_t *wlits = (clingo_weighted_literal_t*) pack[0];
  size_t *i = (size_t*) pack[1];

  /* If we ever accept optimization inside dPASP, we may set p = 0 for ASEO and p > 0 for
   * regular optimization. */

  for (size_t j = 0; j < n; ++j) wlits[*i+j] = W[j];
  *i += n;

  return true;
}

bool control_set_nmodels(clingo_control_t *C, size_t n) {
  clingo_configuration_t *cfg = NULL;
  clingo_id_t cfg_root, cfg_sub;

  /* String to integer. */
#define MAX_N_STR 30
  char n_str[MAX_N_STR + 2];
  size_t i, d;
  n_str[MAX_N_STR+1] = '\0';
  for (i = 0, d = n; d > 9; d /= 10) n_str[MAX_N_STR-(i++)] = '0' + (d % 10);
  n_str[MAX_N_STR-i] = '0' + d;
  char *nmodels = n_str + MAX_N_STR - i;
#undef MAX_N_STR

  if (!clingo_control_configuration(C, &cfg)) return false;
  if (!clingo_configuration_root(cfg, &cfg_root)) return false;
  if (!clingo_configuration_map_at(cfg, cfg_root, "solve.models", &cfg_sub)) return false;
  if (!clingo_configuration_value_set(cfg, cfg_sub, nmodels)) return false;

  return true;
}

/** Probabilistic components to weak rules. */
bool pc2wr(program_t *P, clingo_control_t *C, clingo_backend_t *back, size_t scale) {
  bool ok = false;
  clingo_weighted_literal_t wl = {0};
  clingo_atom_t choice;

  for (size_t i = 0; i < P->PF_n; ++i) {
    wl.literal = P->PF[i].cl_f;
    wl.weight = scale*log(P->PF[i].p/(1-P->PF[i].p));
    if (!clingo_backend_add_atom(back, &P->PF[i].cl_f, &choice)) goto cleanup;
    if (!clingo_backend_rule(back, true, &choice, 1, NULL, 0)) goto cleanup;
    if (!clingo_backend_minimize(back, 0, &wl, 1)) goto cleanup;
  }

  /* Clingo unfortunately does not support adding cardinality constraint bounds that are not lower
   * bounds through backend. So instead, we have to do string translation. Maybe handling the AST
   * might be more efficient, but the AST API is still a mistery to me. */
#define MAX_RULE_LENGTH 8192
  char rule[MAX_RULE_LENGTH];
  size_t offset;
  for (size_t i = 0; i < P->AD_n; ++i) {
    rule[0] = '{'; rule[1] = '\0';
    offset = 1;
    offset += sprintf(rule+offset, "%s", P->AD[i].F[0]);
    for (size_t j = 1; j < P->AD[i].n; ++j) {
      offset += sprintf(rule+offset, ", %s", P->AD[i].F[j]);
      wl.literal = P->AD[i].cl_F[j];
      wl.weight = scale*log(P->AD[i].P[j]/(1-P->AD[i].P[j]));
      if (!clingo_backend_minimize(back, 0, &wl, 1)) goto cleanup;
    }
    rule[offset++] = '}'; rule[offset] = '\0';
    if (!clingo_control_add(C, "base", NULL, 0, rule)) goto cleanup;
  }
#undef MAX_RULE_LENGTH

  ok = true;
cleanup:
  return ok;
}

bool aseo_solve(program_t *P, clingo_control_t *C, size_t k,
    clingo_solve_result_bitset_t *solve_ret, ctree_t *T, size_t *N, model_t *models,
    bool (*f)(const clingo_model_t*, program_t*, ctree_t*, model_t*, clingo_control_t*)) {
  bool ok = false;
  clingo_solve_handle_t *handle;
  const clingo_model_t *M;
  size_t m;

  if (!clingo_control_solve(C, clingo_solve_mode_yield, NULL, 0, NULL, NULL, &handle)) goto cleanup;
  for (m = 0; true; ++m) {
    if (!clingo_solve_handle_resume(handle)) goto cleanup;
    if (!clingo_solve_handle_model(handle, &M)) goto cleanup;
    if (M) {
      ctree_t *leaf = ctree_add(T, M, P);
      if (!leaf) goto cleanup;
      if (!f(M, P, leaf, &models[*N+m], C)) goto cleanup;
    } else break;
  }
  if (!clingo_solve_handle_get(handle, solve_ret)) goto cleanup;

  *N += m;
  ok = true;
cleanup:
  return ok;
}

bool set_upper_bound(clingo_backend_t *back, clingo_weighted_literal_t *W, size_t n,
    clingo_weighted_literal_t *U, int cost) {
  /* We assume there is only one optimization level, so there is only one cost: some objective
   * function that is proportional to the log-likelihood. */
  int l = -cost;
  for (size_t i = 0; i < n; ++i)
    if (W[i].weight > 0) {
      l += W[i].weight;
      U[i].literal = -W[i].literal;
      U[i].weight = W[i].weight;
    } else {
      U[i].literal = W[i].literal;
      U[i].weight = -W[i].weight;
    }
  if (!clingo_backend_begin(back)) return false;
  bool ok = clingo_backend_weight_rule(back, false, NULL, 0, l, U, n);
  if (!clingo_backend_end(back)) return false;
  return ok;
}

model_t* aseo(program_t *P, clingo_control_t *C, size_t k, psemantics_t psem, observations_t *O,
    bool (*f)(const clingo_model_t*, program_t*, ctree_t*, model_t*, clingo_control_t*)) {
  bool ok = false;
  clingo_backend_t *back = NULL;
  clingo_ground_program_observer_t obs = {NULL}; obs.minimize = watch_minimize;
  model_t *M = NULL;

  size_t n = num_prob_params(P);
  clingo_weighted_literal_t *W = (clingo_weighted_literal_t*) malloc(n*sizeof(clingo_weighted_literal_t));
  clingo_weighted_literal_t *U = (clingo_weighted_literal_t*) malloc(n*sizeof(clingo_weighted_literal_t));
  if (!(W && U)) goto nomem;
  M = model_create(k, (!O)*P->Q_n+(O != NULL)*O->n, psem);

  size_t i_W = 0;
  void *pack[] = {(void*) W, (void*) &i_W};
  if (!clingo_control_backend(C, &back)) goto cleanup;
  if (!clingo_control_register_observer(C, &obs, false, (void*) pack)) goto cleanup;
  if (!control_set_nmodels(C, k)) goto cleanup;
  if (!clingo_control_ground(C, GROUND_DEFAULT_PARTS, 1, NULL, NULL)) goto cleanup;

  const clingo_statistics_t *stats;
  uint64_t root_key, costs_key, cost_key;
  if (!clingo_control_statistics(C, &stats)) goto cleanup;
  if (!clingo_statistics_root(stats, &root_key)) goto cleanup;
  if (!clingo_statistics_map_at(stats, root_key, "summary.costs", &costs_key)) goto cleanup;

  ctree_t T = CTREE_INIT;
  clingo_solve_result_bitset_t res;

  size_t m; /* number of models seen so far */
  double cost;
  if (!aseo_solve(P, C, k, &res, &T, &m, M, f)) goto cleanup;
  while ((res & clingo_solve_result_satisfiable) && !(res & clingo_solve_result_interrupted)) {
    if (m >= k) break;
    else if (!control_set_nmodels(C, k-m)) goto cleanup;

    /* If clingo does not update keys on solving, then we can push this line up to the init block. */
    if (!clingo_statistics_array_at(stats, costs_key, 0, &cost_key)) goto cleanup;
    if (!clingo_statistics_value_get(stats, cost_key, &cost)) goto cleanup;

    if (!set_upper_bound(back, W, n, U, (int) cost)) goto cleanup;
    if (!aseo_solve(P, C, k, &res, &T, &m, M, f)) goto cleanup;
  }

  /* Debug: write models to dot. */
  char buffer[8192];
  if (!ctree_dot(&T, P, buffer)) goto cleanup;

  ok = true;
nomem:
  PyErr_SetString(PyExc_MemoryError, "could not allocate enough memory for ASEO!");
cleanup:
  if (clingo_error_code() != clingo_error_success) raise_clingo_error(NULL);
  free(W); free(U);
  ctree_free_contents(&T);
  if (!ok) { model_free(M, k); M = NULL; }
  return M;
}

