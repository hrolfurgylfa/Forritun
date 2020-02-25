#include "Nemandi.h"
#include <iostream>


///////////////////
// Constructors //
/////////////////

Nemandi::Nemandi(){
    this->id = 0;
    this->nafn = "";
}

Nemandi::Nemandi(int id, std::string nafn){
    this->id = id;
    this->nafn = nafn;
}


/////////////////////////
// Getters og Setters //
///////////////////////

int Nemandi::get_id(){ return this->id; }
void Nemandi::set_id(int id){ this->id = id; }

std::string Nemandi::get_nafn(){ return this->nafn; }
void Nemandi::set_nafn(std::string nafn){ this->nafn = nafn; }


///////////////////
// cout support //
/////////////////

std::ostream& operator<<(std::ostream& ostr, Nemandi& Nemandi){
    return ostr
    << "ID: " << Nemandi.get_id()
    << " Nafn: " << Nemandi.get_nafn();
}