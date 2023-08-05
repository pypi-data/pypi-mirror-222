#ifndef _PASP_CASEO
#define _PASP_CASEO

#include <stdbool.h>
#include "cprogram.h"
#include "cinf.h"

/**
 * Answer Set Enumeration by Optimality (ASEO).
 */

bool approx_aseo(program_t *P, double **R, psemantics_t psem, bool quiet, bool status);

#endif
