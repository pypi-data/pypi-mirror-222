#ifndef _PASP_CAPPROX
#define _PASP_CAPPROX

#include <clingo.h>

#include "cprogram.h"
#include "ctree.h"
#include "cmodel.h"

bool query_maxent(const clingo_model_t *cM, program_t *P, ctree_t *T, model_t *M,
    clingo_control_t *C);
bool query_credal(const clingo_model_t *cM, program_t *P, ctree_t *T, model_t *M,
    clingo_control_t *C);

#endif
