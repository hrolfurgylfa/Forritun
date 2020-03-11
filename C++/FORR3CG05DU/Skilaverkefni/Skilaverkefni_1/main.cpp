// Class Headers
#include "Afangi.h"
#include "Nemandi.h"

// Class Functions
#include "Afangi.hpp"
#include "Nemandi.hpp"


#include <iostream>
#include <string>


int main(){

    std::cout << "Forrit byrjað\n\n" << std::flush;

    Nemandi c = Nemandi(1, "Jón");

    c.baeta_vid_afanga(1, "ROB100", 9);
    c.baeta_vid_afanga(2, "STÆ500", 7);
    c.baeta_vid_afanga(3, "STÆ600");
    c.baeta_vid_afanga(4, "FOR100", 9.5);
    c.baeta_vid_afanga(5, "DAN100", 3.5);
    c.baeta_vid_afanga(6, "FOR200", 9.86);

    c.fara_ur_afanga("FOR100");
    c.fara_ur_afanga(2);

    c.prenta();

    std::cout << "\nForrit búið" << std::flush;

    return 0;
}