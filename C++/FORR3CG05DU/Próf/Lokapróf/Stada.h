#include <iostream>
#include <string>

#ifndef STADA_H
#define STADA_H

class Stada
{
private:
    char stada;
    std::string nafn;
public:
    Stada();
    Stada(char stada, std::string nafn);

    char get_stada();
    void set_stada(char stada);
    
    std::string get_nafn();
    void set_nafn(std::string nafn);
};

#endif