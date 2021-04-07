int sum(int a, int b);

void hello(const char *name);

struct my_struct_t
{
    unsigned int uid;
    unsigned int time;
    char a;
    char b;
    char c;
    char d;
};

typedef struct my_struct_t my_struct;

void print_struct(my_struct *s);
