#include "cmodel.h"

#include <stdio.h>

bool model_init(model_t *M, size_t n, size_t m, psemantics_t credal) {
  size_t k = (credal == CREDAL_SEMANTICS)*4+(credal == MAXENT_SEMANTICS)*2;

  for (size_t i = 0; i < n; ++i)
    if (!(M[i].Q = bitvec_create(m*k))) {
      for (size_t j = 0; j < i; ++j) bitvec_free(M[j].Q);
      return false;
    }

  return true;
}

model_t* model_create(size_t n, size_t m, psemantics_t psem) {
  model_t *M = (model_t*) malloc(n*sizeof(model_t));
  if (!M) return NULL;
  if (!model_init(M, n, m, psem)) { free(M); return NULL; }
  return M;
}

void model_free_contents(model_t *M, size_t n) {
  if (!M) return;
  for (size_t i = 0; i < n; ++i) bitvec_free(M[i].Q);
}
void model_free(model_t *M, size_t n) { model_free_contents(M, n); free(M); }
