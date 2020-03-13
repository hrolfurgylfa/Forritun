#include "Node.h"

#include <iostream>

Node::Node(){
    this->tala = 0;
    this->next = nullptr;
}
Node::Node(int tala){
    this->tala = tala;
    this->next = nullptr;
}

Node* Node::get_next(){ return this->next; }
void Node::set_next(Node* node_ptr){ this->next = node_ptr; }

int Node::get_tala(){ return this->tala; }
void Node::set_tala(int tala){ this->tala = tala; }