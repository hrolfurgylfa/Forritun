#include <iostream>
#include "Dyr.h"

using namespace std;

class A {
  private:
    int tala;
  public:
    A() : tala(-1) {}
    A(int tala) : tala(tala) {}
    int getTala() { return this->tala; }
    virtual void prenta() { cout << "A: " << this->tala << endl; }
    virtual ~A() {}
};

class B : public A {
  public:
    B() {}
    B(int tala) : A(tala) {}
    void prenta() { cout << "B: " << this->getTala() << endl; }
};

class C : public A {
  public:
    C() {}
    C(int tala) : A(tala) {}
    void prenta() { cout << "C: " << this->getTala() << endl; }  
};

struct ANode {
  A* data;
  ANode* next;
  ANode() : data(nullptr), next(nullptr) {}
  ANode(A* data) : data(data), next(nullptr) {}
};

class HT {
  private:
    ANode** taflan; 
  public:
    HT() { this->taflan = new ANode*[3](); }
    int hash(int data) { return data % 3; }
    void setjaItoflu(A* data) {
      int index = this->hash(data->getTala());
      if(this->taflan[index] == nullptr)
        this->taflan[index] = new ANode(data);
      else {
        ANode* current = this->taflan[index];
        while(current->next)
          current = current->next;
        current->next = new ANode(data);
      }
    }
};

int main() {
  HT ht;
  ht.setjaItoflu(new B(10));
  ht.setjaItoflu(new C(11));
  ht.setjaItoflu(new A(12));
  ht.setjaItoflu(new B(13));
  ht.setjaItoflu(new C(14));
  ht.setjaItoflu(new A(15));
  
  return 0;
}