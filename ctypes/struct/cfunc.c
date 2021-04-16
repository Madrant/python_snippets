#ifdef __cplusplus
extern "C" {
#endif

#include <stdio.h>

#include "cfunc.h"

#define FUNC_START printf("%s: START\n", __PRETTY_FUNCTION__);
#define FUNC_END   printf("%s: END\n", __PRETTY_FUNCTION__);

void print_message(message *m)
{
    printf("message:\n");

    printf("\tuid:  %u\n", m->uid);
    printf("\ttime: %u\n", m->time);

    printf("\ta:    %c\n", m->a);
    printf("\tb:    %c\n", m->b);
    printf("\tc:    %c\n", m->c);
    printf("\td:    %c\n", m->d);
}

int process(message &m)
{
    FUNC_START;

    print_message(&m);

    FUNC_END;

    return (int)m.uid;
}

int process_array(message *message_array, int messages)
{
    FUNC_START;

    for (int i = 0; i < messages; i++)
    {
        message* m = &message_array[i];

        print_message(m);

        m->a = 't';
        m->b = 'e';
        m->c = 's';
        m->d = 't';
    }

    return 0;

    FUNC_END;
}

#ifdef __cplusplus
} // extern C
#endif
