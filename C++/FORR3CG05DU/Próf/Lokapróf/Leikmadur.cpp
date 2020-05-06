#include <iostream>
#include <string>
#include "Leikmadur.h"

Leikmadur::Leikmadur(){
    this->id = 0;
    this->nafn = "";
}
Leikmadur::Leikmadur(int id, std::string nafn){
    this->id = id;
    this->nafn = nafn;
}

// Getters og setters
int Leikmadur::get_id(){ return this->id; }
void Leikmadur::set_id(int id){ this->id = id; }

std::string Leikmadur::get_nafn(){ return this->nafn; }
void Leikmadur::set_nafn(std::string nafn){ this->nafn = nafn; }

// Overloads
std::ostream& operator<<(std::ostream& ostr, Leikmadur& leikmadur){
    return ostr << "ID: " << leikmadur.get_id()
                << ", Nafn: " << leikmadur.get_nafn();
}