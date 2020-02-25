#include "Afangi.h"
#include <iostream>


///////////////////
// Constructors //
/////////////////

Afangi::Afangi(){
    this->id = 0;
    this->nafn = "";
    this->einkunn = 0;
}

Afangi::Afangi(int id, std::string nafn, float einkunn){
    this->id = id;
    this->nafn = nafn;
    this->einkunn = einkunn;
}


/////////////////////////
// Getters og Setters //
///////////////////////

int Afangi::get_id(){ return this->id; }
void Afangi::set_id(int id){ this->id = id; }

std::string Afangi::get_nafn(){ return this->nafn; }
void Afangi::set_nafn(std::string nafn){ this->nafn = nafn; }

float Afangi::get_einkunn(){ return this->einkunn; }
void Afangi::set_einkunn(float einkunn){ this->einkunn = einkunn; }


///////////////////
// cout support //
/////////////////

std::ostream& operator<<(std::ostream& ostr, Afangi& afangi){
    return ostr
    << "ID: " << afangi.get_id()
    << " Áfangi: " << afangi.get_nafn()
    << " Einkunn: " << afangi.get_einkunn();
}