#ifndef NODE_H
#define NODE_H

class Node
{
private:
    int tala;
    Node* next;

public:
    Node();
    Node(int tala);

    Node* get_next();
    void set_next(Node* node_ptr);

    int get_tala();
    void set_tala(int tala);
};

#endif