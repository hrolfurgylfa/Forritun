#ifndef NEMANDI_SKIL_1_CLASS
#define NEMANDI_SKIL_1_CLASS

#include <iostream>
#include "Afangi.h"

class Nemandi {
public:
    //Constructors
    Nemandi();
    Nemandi(int id, std::string nafn);
    ~Nemandi();


    // Getters and setters
    int get_id();
    void set_id(int id);

    std::string get_nafn();
    void set_nafn(std::string nafn);


    // Functions
    void baeta_vid_afanga(int id, std::string nafn);
    void baeta_vid_afanga(int id, std::string nafn, float einkunn);

    void fara_ur_afanga(int id);
    void fara_ur_afanga(std::string nafn);
    
    float medaleinkunn();
    void prenta();
    void prenta_afanga(int id);
    void prenta_alla_afanga();


    // Overloads
    bool operator==(Nemandi& other);
    bool operator!=(Nemandi& other);

private:
    int id;
    std::string nafn;

    Afangi* afanga_listi;
    int afanga_listi_lengd;

    void staekka_afanga_lista();
    Afangi* finna_afanga(int id);
    void baeta_vid_afanga(Afangi afangi);
};

std::ostream& operator<<(std::ostream& ostr, Nemandi& flight);

#endif