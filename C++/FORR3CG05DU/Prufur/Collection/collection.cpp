#include <iostream>
#include <string>

class IntList {
    private:
        int* list;
        int length;
    public:
        IntList() {
            this->list = new int[0];
            this->length = 0;
        }
        ~IntList() {
            delete [] this->list;
        }
        void append(int number) {
            int* old_list = this->list;
            int* new_list = new int[this->length+1];

            for (int i = 0; i < this->length; i++) {
                new_list[i] = old_list[i];
            }

            new_list[length] = number;
            this->list = new_list;
            this->length++;

            delete [] old_list;
        }
        int* get() { return list; }
        int get(int item_number) { return list[item_number]; }
        void print() {
            for (int i = 0; i < this->length; i++){

            }
        }
};
void testIntList() {
    IntList* tolu_listi = new IntList();
    std::cout << "Tolu listi fyrir viðbæslu: " << &tolu_listi.get() << "\n" << std::flush;
    *tolu_listi.append(3);
    *tolu_listi.append(7);
    std::cout << "Tolu listi eftir viðbæslu: " << tolu_listi.get() << "\n" << std::flush;
}
int main() {
    testIntList();
}