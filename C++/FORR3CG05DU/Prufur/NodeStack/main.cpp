// Stack klasi
#include "NodeStack.h"
#include "Node.h"

// Default libraries
#include <iostream>
#include <string>


int main(){
    NodeStack stack;
    stack.push(10);
    stack.push(15);
    stack.push(3);
    std::cout << "Current stack node: " << stack.peek() << "\n" << std::flush;
    stack.pop();
    stack.prenta();
}