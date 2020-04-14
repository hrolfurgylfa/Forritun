#include <iostream>
#include <string>


class A {
public:
    int tala;

    A() {
        this->tala = 0;
    }
    A(int tala) {
        this->tala = tala;
    }
    virtual void prenta() {
        std::cout << this->tala;
    }
};

class B : public A {
public:
    void prenta() {
        std::cout << this->tala;
    }
};

class C : public A {
public:
    void prenta() {
        std::cout << this->tala;
    }
};

class AListi {
private:
    A** listinn;
    int staerd;
    int fjoldi;
public:
    AListi() {
        this->fjoldi = 0;
        this->staerd = 2;
        this->listinn = new A*[this->staerd];
    }
    ~AListi() {
        for (int i = 0; i < this->fjoldi; i++)
            delete this->listinn[i];
        
        delete [] this->listinn;
    }

    void append(A* a_ptr) {
        if (this->fjoldi < this->staerd) {
            this->listinn[this->fjoldi] = a_ptr;
            this->fjoldi++;
        } 
        else {
            this->staerd += 2;
            A** old_list = this->listinn;
            A** new_list = new A*[this->staerd];

            for (int i = 0; i < this->fjoldi; i++) {
                new_list[i] = old_list[i];
            }

            new_list[this->fjoldi] = a_ptr;
            this->listinn = new_list;
            this->fjoldi++;

            delete [] old_list;
        }
    }

    void add_b() { this->append(new B()); }
    void add_c() { this->append(new C()); }

    void prenta() {
        for (int i = 0; i < this->fjoldi; i++)
            this->listinn[i]->prenta();
    }
};


int main() {
    std::cout << "Program started." << "\n" << std::flush;

    AListi listi = AListi();

    std::cout << "Program finished." << "\n" << std::flush;
    return 0;
}