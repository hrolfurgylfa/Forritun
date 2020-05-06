#include <iostream>
#include <string>
#include "Leikmadur.h"
#include "Stada.h"

#ifndef VISTARLEIKMADUR_H
#define VISTARLEIKMADUR_H

class VistarLeikmadur : public Leikmadur
{
private:
    int stig;
    Stada stada;
public:
    VistarLeikmadur(int id, std::string nafn, int stig, Stada stada);

    // Getters og setters
    int get_stig();
    void set_stig(int stig);

    Stada get_stada();
    void set_stada(Stada stada);

    // Overloads
    bool operator>(VistarLeikmadur& other);
    bool operator<(VistarLeikmadur& other);
    bool operator>=(VistarLeikmadur& other);
    bool operator<=(VistarLeikmadur& other);

    bool operator==(VistarLeikmadur& other);
    bool operator!=(VistarLeikmadur& other);
};

std::ostream& operator<<(std::ostream& ostr, VistarLeikmadur& leikmadur);

#endif