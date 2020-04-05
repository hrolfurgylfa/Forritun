#include <iostream>

#include"RadadurListi.h"
#include "Verkefni.h"

int main() {
    std::cout << "Forrit byrjar!" << "\n\n" << std::flush;

    RadadurListi listi;

    std::cout << "Öll tasks:" << "\n" << std::flush;
    listi.append(Verkefni("Vinna á Udon LPD Station", false, 2));
    std::cout << "Added num 4" << "\n" << std::flush;
    listi.append(Verkefni("Klára Skilaverkefni 2 C++", true, 5));
    std::cout << "Added num 1" << "\n" << std::flush;
    // listi.append(Verkefni("Klára Skilaverkefni 3 C++", true, 5));
    // std::cout << "Added num 2" << "\n" << std::flush;
    listi.append(Verkefni("Vinna á Dev Team Applications", false, 4));
    std::cout << "Added num 3" << "\n" << std::flush;
    listi.print();

    std::cout << "C++ klárað:" << "\n" << std::flush;
    // listi.remove("Klára Skilaverkefni 2 C++");
    // listi.remove("Klára Skkilaverkefni 3 C++");
    // listi.remove("Vinna á Dev Team Applications");
    // listi.remove("Vinna á Udon LPD Station");
    listi.print();

    std::cout << "Forrit búið!" << std::flush;
    return 0;
}