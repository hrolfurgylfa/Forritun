#include <iostream>

class Stack {
private:
    int stack[10];
    int pos;

public:
    Stack();
    ~Stack();

    void push(int tala);
    void pop();
    int peek();
    void prenta();
};
