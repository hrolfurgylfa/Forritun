#include "stack.h"


Stack::Stack(){}
Stack::~Stack(){}

void Stack::push(int tala){
    this->pos++;
    this->stack[this->pos] = tala;
}
void Stack::pop(){
    if (this->pos > 0) this->pos--;
    this->stack[this->pos] = 0;
}
int Stack::peek(){
    return this->stack[this->pos];
}
void Stack::prenta(){
    for (int i = 0; i < 10; i++) {
        std::cout << this->stack[i] << " ";
    }
}