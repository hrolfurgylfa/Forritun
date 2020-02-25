// Class Headers
#include "Afangi.h"
#include "Nemandi.h"

// Class Functions
#include "Afangi.hpp"
#include "Nemandi.hpp"


#include <iostream>
#include <string>


int main(){

    Afangi a = Afangi(1, "FORR1", 9);
    Afangi b = Afangi(2, "FORR2", 3);
    Nemandi c = Nemandi(1, "Jón");
    Nemandi d = Nemandi(2, "Jónína");

    std::cout << a << "\n" << b << "\n\n" << std::flush;
    std::cout << c << "\n" << d << "\n" << std::flush;

    return 0;
}