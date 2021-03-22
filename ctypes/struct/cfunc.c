#ifdef __cplusplus
extern "C" {
#endif

#include "cfunc.h"

int process(message &m)
{
    return (int)m.uid;
}

#ifdef __cplusplus
} // extern C
#endif
