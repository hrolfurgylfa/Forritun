#include <iostream>

#include"RadadurListi.h"
#include "Verkefni.h"

int main() {
    std::cout << "Forrit byrjar!" << "\n\n" << std::flush;

    RadadurListi listi;

    // Bæta öllu við
    std::cout << "Öll tasks:" << "\n" << std::flush;
    listi.append(Verkefni("Vinna á Udon LPD Station", false, 2));
    listi.append(Verkefni("Klára Skilaverkefni 2 C++", true, 5));
    listi.append(Verkefni("Klára Skilaverkefni 3 C++", true, 5));
    listi.append(Verkefni("Vinna á Dev Team Applications", false, 4));
    listi.print();
    std::cout << "\n" << std::flush;

    // Eyða einu og prenta bara skóla áfanga
    std::cout << "C++ klárað og bara skóla verkefni:" << "\n" << std::flush;
    listi.remove("Klára Skilaverkefni 2 C++");
    // listi.remove("Klára Skkilaverkefni 3 C++");
    // listi.remove("Vinna á Dev Team Applications");
    // listi.remove("Vinna á Udon LPD Station");
    listi.print_school(true);
    std::cout << "\n" << std::flush;

    // Sækja næsta verkefni og eyða því úr listanum
    std::cout << "Sækja næsta verkefni:" << "\n" << std::flush;
    Verkefni return_verkefni = listi.fetch_next();
    return_verkefni.prenta_verkefni();
    std::cout << "\n" << std::flush;

    // Prennta allt
    std::cout << "Öll verkefni:" << "\n" << std::flush;
    listi.print();
    std::cout << "\n" << std::flush;

    std::cout << "Forrit búið!" << std::flush;
    return 0;
}