struct message_t
{
    unsigned int uid;
    unsigned int time;
    char a;
    char b;
    char c;
    char d;
};

typedef struct message_t message;

int process(message &m);
