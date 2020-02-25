#include "Nemandi.h"
#include "Afangi.h"
#include <iostream>


///////////////////
// Constructors //
/////////////////

Nemandi::Nemandi(){
    this->id = 0;
    this->nafn = "";

    this->afanga_listi = new Afangi[2];
    this->afanga_listi_lengd = sizeof(afanga_listi) / sizeof(afanga_listi[0]);
}

Nemandi::Nemandi(int id, std::string nafn){
    this->id = id;
    this->nafn = nafn;

    this->afanga_listi = new Afangi[2];
    this->afanga_listi_lengd = sizeof(afanga_listi) / sizeof(afanga_listi[0]);
}

Nemandi::~Nemandi(){
    delete [] this->afanga_listi;
}


/////////////////////////
// Getters og Setters //
///////////////////////

int Nemandi::get_id(){ return this->id; }
void Nemandi::set_id(int id){ this->id = id; }

std::string Nemandi::get_nafn(){ return this->nafn; }
void Nemandi::set_nafn(std::string nafn){ this->nafn = nafn; }


////////////////////////
// Private functions //
//////////////////////

void Nemandi::staekka_afanga_lista(){

    Afangi* old_list = this->afanga_listi;

    int new_length = this->afanga_listi_lengd+2;
    Afangi* new_list = new Afangi[new_length];

    for (int i = 0; i < this->afanga_listi_lengd; i++) {
        new_list[i] = old_list[i];
    }

    this->afanga_listi = new_list;
    this->afanga_listi_lengd = new_length;

    delete [] old_list;
}

Afangi* Nemandi::finna_afanga(int id){

    Afangi* fundinn_afangi = NULL;

    for (int i = 0; i < this->afanga_listi_lengd; i++) {
        if (afanga_listi[i].get_id() == id) {
            fundinn_afangi = &afanga_listi[i];
            break;
        }
    }

    return fundinn_afangi;
}

void Nemandi::baeta_vid_afanga(Afangi* afangi){
    Afangi* tomur_afanga_ptr = finna_afanga(0);
    if (tomur_afanga_ptr) {
        tomur_afanga_ptr = afangi;
    } else {
        this->staekka_afanga_lista();
        Afangi* tomur_afanga_ptr = finna_afanga(0);
        tomur_afanga_ptr = afangi;
    }
}


///////////////////////
// Public functions //
/////////////////////

std::string Nemandi::baeta_vid_afanga(int id, std::string nafn){

    
}
std::string Nemandi::baeta_vid_afanga(int id, std::string nafn, float einkunn){

}

std::string Nemandi::fara_ur_afanga(int id){

}
std::string Nemandi::fara_ur_afanga(std::string nafn){

}


////////////////
// Overloads //
//////////////

bool Nemandi::operator==(Nemandi& other){ return this->id == other.id; }
bool Nemandi::operator!=(Nemandi& other){ return !(*this == other); }


///////////////////
// cout support //
/////////////////

std::ostream& operator<<(std::ostream& ostr, Nemandi& Nemandi){
    return ostr
    << "ID: " << Nemandi.get_id()
    << " Nafn: " << Nemandi.get_nafn();
}