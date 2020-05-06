#include <iostream>
#include <string>
#include "Stada.h"

Stada::Stada(){
    this->stada = '0';
    this->nafn = "";
}
Stada::Stada(char stada, std::string nafn){
    this->stada = stada;
    this->nafn = nafn;
}

char Stada::get_stada(){ return this->stada; }
void Stada::set_stada(char stada){ this->stada = stada; }

std::string Stada::get_nafn(){ return this->nafn; }
void Stada::set_nafn(std::string nafn){ this->nafn = nafn; }