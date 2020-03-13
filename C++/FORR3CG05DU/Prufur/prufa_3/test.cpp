#include <iostream>
#include <string>

int main() {
  
    int* a = new int[5];

    a[1] = 2;
    a[3] = 3;
    
    std::cout << a[1];

    a[1] = 6;

    std::cout << a[1];

    return 0;
}