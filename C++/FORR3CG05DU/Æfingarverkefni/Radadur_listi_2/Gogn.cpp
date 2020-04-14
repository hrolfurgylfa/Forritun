#include "Gogn.h"

Gogn::Gogn() {
    this->id = -1;
    this->numer = -1;
}

Gogn::Gogn(int id, int numer) {
    this->id = id;
    this->numer = numer;
}


int Gogn::getID() {
    return this->id;
}

void Gogn::prentaGogn() {
    cout << "ID: " << this->id << ", Numer: " << this->numer << endl;
}

int Gogn::getNumer() {
    return this->numer;
}

bool Gogn::operator<(Gogn& other) { return this->numer < other.numer; }

// Fallið skilar true ef numer í þessum klasa er stærra en numer í other
bool Gogn::operator>(Gogn& other) { return other < *this; }

// Fallið skilar true ef numer í þessum klasa er minna eða sama sem numer í other
bool Gogn::operator<=(Gogn& other) { return !(*this > other); }

// Fallið skilar true ef numer í þessum klasa er stærra eða sama sem numer í other
bool Gogn::operator>=(Gogn& other) { return !(*this < other); }

// Fallið skilar true ef numer í þessum klasa er sama sem numer í other
bool Gogn::operator==(Gogn& other) { return this->id == other.id; }

// Fallið skilar true ef numer í þessum klasa er ekki sama sem numer í other
bool Gogn::operator!=(Gogn& other) { return !(*this == other); }

