// Stack klasi
#include "stack.hpp"
// #include "stack.h"


#include <iostream>
#include <string>


int main(){
    Stack stack;
    stack.push(10);
    stack.push(15);
    stack.push(3);
    stack.peek();
    stack.pop();
    stack.prenta();
}