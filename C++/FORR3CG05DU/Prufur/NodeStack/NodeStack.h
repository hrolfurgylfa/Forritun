#ifndef NODE_STACK_H
#define NODE_STACK_H

#include "Node.h"

class NodeStack
{
private:
    Node* stafli;

public:
    NodeStack();
    ~NodeStack();

    void push(int tala);
    void pop();
    int peek();
    void prenta();
};

#endif