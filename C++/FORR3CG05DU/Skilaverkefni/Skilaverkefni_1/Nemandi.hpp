#include "Nemandi.h"
#include "Afangi.h"
#include <iostream>
#include <math.h>


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
        if (this->afanga_listi[i].get_id() == id) {
            fundinn_afangi = &afanga_listi[i];
            break;
        }
    }

    return fundinn_afangi;
}

void Nemandi::baeta_vid_afanga(Afangi afangi){
    Afangi* tomur_afanga_ptr = finna_afanga(0);

    if (tomur_afanga_ptr) *tomur_afanga_ptr = afangi;
    else {
        this->staekka_afanga_lista();
        *finna_afanga(0) = afangi;
    }
}


///////////////////////
// Public functions //
/////////////////////

void Nemandi::baeta_vid_afanga(int id, std::string nafn){
    this->baeta_vid_afanga(Afangi(id, nafn));
}
void Nemandi::baeta_vid_afanga(int id, std::string nafn, float einkunn){
    this->baeta_vid_afanga(Afangi(id, nafn, einkunn));
}

void Nemandi::fara_ur_afanga(int id){
    for (int i = 0; i < this->afanga_listi_lengd; i++){
        if (this->afanga_listi[i].get_id() == id) afanga_listi[i] = Afangi();
    }
}
void Nemandi::fara_ur_afanga(std::string nafn){
    for (int i = 0; i < this->afanga_listi_lengd; i++){
        if (this->afanga_listi[i].get_nafn() == nafn) afanga_listi[i] = Afangi();
    }
}

float Nemandi::medaleinkunn(){
    int fjoldi_einkanna = 0;
    float summa_einkanna = 0;

    for (int i = 0; i < this->afanga_listi_lengd; i++){
        if (afanga_listi[i].get_id() != 0){
            fjoldi_einkanna++;
            summa_einkanna += afanga_listi[i].get_einkunn();
        }
    }

    // Reikna meðaleinkunnina
    float medaleinkunn = summa_einkanna/fjoldi_einkanna;

    // Námunda meðaleinkunnina, ég fann þennan útreikning hérna https://stackoverflow.com/a/14369745
    // en ég breytti honum vegna þess að ég þarf ekki að reikna mínustölur og ég vill ekki
    // nota annað fall til þess að reikna þetta. Það sem þetta gerir er að þetta hækkar töluna um
    // hundrað til þess að geyma tvo aukastafina í tölunni, ekki fyrir aftan sem aukastafi, svo þarf að
    // hækka töluna um 0.5 til þess að nota floor sem námundun ekki bara setja töluna niður og svo deili
    // ég með hundrað til þess að fá tvo aukastafina sem ég var að geyma aftur.
    float rounded_medaleinkunn = floor(( medaleinkunn * 100.0 ) + 0.5) / 100.0;
    
    return rounded_medaleinkunn;
}
void Nemandi::prenta(){
    std::cout
    << "Nemenda ID: " << this->get_id()
    << " Nafn: " << this->get_nafn()
    << " Áfangar:\n" << std::flush;
    this->prenta_alla_afanga();
    std::cout << "Meðaleinkunn: " << this->medaleinkunn() << "\n" << std::flush;
}
void Nemandi::prenta_afanga(int id){
    Afangi* fundinn_afangi = this->finna_afanga(id);
    
    if (fundinn_afangi == NULL){
        std::cout << "Áfangi ekki fundinn.\n" << std::flush;
        return;
    }

    std::cout << *fundinn_afangi << "\n" << std::flush;
}
void Nemandi::prenta_alla_afanga(){
    for (int i = 0; i < this->afanga_listi_lengd; i++) {
        if (this->afanga_listi[i].get_id() != 0)
            std::cout << this->afanga_listi[i] << "\n" << std::flush;
    }
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