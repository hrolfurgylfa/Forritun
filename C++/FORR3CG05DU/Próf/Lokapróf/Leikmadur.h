#include <iostream>
#include <string>
#include "Stada.h"

#ifndef LEIKMADUR_H
#define LEIKMADUR_H

class Leikmadur
{
protected:
    int id;
    std::string nafn;
public:
    Leikmadur();
    Leikmadur(int id, std::string nafn);

    // Getters og setters
    int get_id();
    void set_id(int id);

    std::string get_nafn();
    void set_nafn(std::string nafn);
};

std::ostream& operator<<(std::ostream& ostr, Leikmadur& leikmadur);

#endif