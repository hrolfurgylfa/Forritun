#include "Gogn.h"

Gogn::Gogn() {
    this->id = -1;
    this->numer = -1;
}

Gogn::Gogn(int id, int numer) {
    this->id = id;
    this->numer = numer;
}

int Gogn::getID() { return this->id; }
int Gogn::getGogn() { return this->numer; }

void Gogn::prentaGogn() {
    cout << "ID: " << this->id << ", Numer: " << this->numer << endl;
}

bool Gogn::operator>(Gogn& other){ return this->numer > other.numer; }
bool Gogn::operator<(Gogn& other){ return other > *this; }
bool Gogn::operator>=(Gogn& other){ return !(*this < other); }
bool Gogn::operator<=(Gogn& other){ return !(*this > other); }

bool Gogn::operator==(Gogn& other){ return this->id == other.id; }
bool Gogn::operator!=(Gogn& other){ return !(*this == other); }

std::ostream& operator<<(std::ostream& ostr, Gogn& gogn){
    return ostr << "ID: " << gogn.getID() << ", Numer: " << gogn.getGogn() << "\n" << std::flush;
}