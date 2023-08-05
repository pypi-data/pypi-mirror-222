#ifndef _PASP_CMODEL
#define _PASP_CMODEL

#include "ctree.h"
#include "cinf.h"
#include "../bitvector/bitvector.h"

/** A model struct for dealing with approximate inference. */
typedef struct {
  /** Bitvector containing true and false values for the queries of each model (a, b, c and d's). */
  bitvec_t *Q;
  /** Model count and probability as represented as a ctree_t leaf. */
  ctree_t *L;
} model_t;

/** Initialize models, where n is the number of models in M, n is the number of queries or
 * observations and psem representing the probabilistic semantics being used. */
bool model_init(model_t *M, size_t n, size_t m, psemantics_t psem);
/** Create models, where n is the number of models in M, n is the number of queries or observations
 * and psem representing the probabilistic semantics being used. */
model_t* model_create(size_t n, size_t m, psemantics_t psem);

void model_free(model_t *M, size_t n);
void model_free_contents(model_t *M, size_t n);

#endif
