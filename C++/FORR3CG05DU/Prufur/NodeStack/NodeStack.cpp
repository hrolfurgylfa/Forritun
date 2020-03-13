#include "NodeStack.h"
#include "Node.h"

#include <iostream>

NodeStack::NodeStack(){
    this->stafli = nullptr;
}
NodeStack::~NodeStack(){
    if (this->stafli == nullptr) return;

    while (this->stafli != nullptr) this->pop();
}

void NodeStack::push(int tala){
    if (this->stafli == nullptr)
        this->stafli = new Node(tala);
    else {
        Node* new_node = new Node(tala);
        new_node->set_next(this->stafli);
        this->stafli = new_node;
    }
}
void NodeStack::pop(){
    if (this->stafli == nullptr) return;

    Node* nyr_stafli = this->stafli->get_next();
    delete this->stafli;
    this->stafli = nyr_stafli;
}
int NodeStack::peek(){
    if (this->stafli != nullptr)
        return this->stafli->get_tala();
    else return -1;
}
void NodeStack::prenta(){
    if (this->stafli == nullptr) {
        std::cout << "Staflinn er tómur.\n" << std::flush;
        return;
    }

    Node* current_node = this->stafli;
    while (current_node != nullptr) {
        std::cout << current_node->get_tala() << " " << std::flush;
        current_node = current_node->get_next();
    }
    std::cout << "\n" << std::flush;
}