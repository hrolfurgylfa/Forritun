#include <iostream>
#include <string>
#include "VistarLeikmadur.h"

VistarLeikmadur::VistarLeikmadur(int id, std::string nafn, int stig, Stada stada){
    this->id = id;
    this->nafn = nafn;
    this->stig = stig;
    this->stada = stada;
}

// Getters og setters
int VistarLeikmadur::get_stig(){ return this->stig; }
void VistarLeikmadur::set_stig(int stig){ this->stig = stig; }

Stada VistarLeikmadur::get_stada(){ return this->stada; }
void VistarLeikmadur::set_stada(Stada stada){ this->stada = stada; }

// Overloads
bool VistarLeikmadur::operator>(VistarLeikmadur& other){ return this->stig > other.stig; }
bool VistarLeikmadur::operator<(VistarLeikmadur& other){ return other > *this; }
bool VistarLeikmadur::operator>=(VistarLeikmadur& other){ return !(*this < other); }
bool VistarLeikmadur::operator<=(VistarLeikmadur& other){ return !(*this > other); }

bool VistarLeikmadur::operator==(VistarLeikmadur& other){ return this->stig == other.stig; }
bool VistarLeikmadur::operator!=(VistarLeikmadur& other){ return !(*this == other); }

std::ostream& operator<<(std::ostream& ostr, VistarLeikmadur& leikmadur){
    return ostr << "ID: " << leikmadur.get_id()
                << ", Nafn: " << leikmadur.get_nafn() 
                << ", Staða: " << leikmadur.get_stada().get_nafn()
                << ", Stig: " << leikmadur.get_stig();
}