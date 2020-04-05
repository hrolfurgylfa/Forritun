#include "Verkefni.h"

Verkefni::Verkefni() {
    this->lysing = "";
    this->er_skola = false;
    this->mikilvaegi = 1;
}
Verkefni::Verkefni(Verkefni* verkefni){
    this->lysing = verkefni->lysing;
    this->er_skola = verkefni->er_skola;
    this->mikilvaegi = verkefni->mikilvaegi;
}
Verkefni::Verkefni(std::string lysing, bool er_skola, int mikilvaegi) {
    this->lysing = lysing;
    this->er_skola = er_skola;
    this->mikilvaegi = mikilvaegi;
}

// Getters og setters
std::string Verkefni::get_lysing() { return this->lysing; }
bool Verkefni::get_er_skola() { return this->er_skola; }
int Verkefni::get_mikilvaegi() { return this->mikilvaegi; }
int Verkefni::get_uniqe_mikilvaegi(){ return this->mikilvaegi + (5 * this->er_skola); }

// Önnur föll
void Verkefni::prenta_verkefni() { std::cout << *this; }

// Overloads
bool Verkefni::operator>(Verkefni& other){ return this->get_uniqe_mikilvaegi() > other.get_uniqe_mikilvaegi(); }
bool Verkefni::operator<(Verkefni& other){ return other > *this; }
bool Verkefni::operator>=(Verkefni& other){ return !(*this < other); }
bool Verkefni::operator<=(Verkefni& other){ return !(*this > other); }

bool Verkefni::operator==(Verkefni& other){ return this->lysing == other.lysing; }
bool Verkefni::operator!=(Verkefni& other){ return !(*this == other); }

std::ostream& operator<<(std::ostream& ostr, Verkefni& Verkefni){
    std::string skola_strengur;
    if (Verkefni.get_er_skola()) skola_strengur = "Þetta er skóla verkefni";
    else skola_strengur = "Þetta er ekki skóla verkefni";

    return ostr << "Mikilvægi: " << Verkefni.get_mikilvaegi() << "\n"
    << skola_strengur << "\n"
    << "Verkefna lýsing: " << Verkefni.get_lysing() << "\n" << std::flush;
}