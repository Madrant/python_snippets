#ifdef __cplusplus
extern "C" {
#endif

#include <stdio.h>

#include "cfunc.h"

int sum(int a, int b)
{
    return a + b;
}

void hello(const char *name)
{
    printf("Hello, %s\r\n", name);
}

void print_struct(my_struct *s)
{
    printf("my structure:\r\n");

    printf("\tuid:  %u\r\n", s->uid);
    printf("\ttime: %u\r\n", s->time);

    printf("\ta: %c\r\n", s->a);
    printf("\tb: %c\r\n", s->b);
    printf("\tc: %c\r\n", s->c);
    printf("\td: %c\r\n", s->d);
}

#ifdef __cplusplus
} // extern C
#endif
