#ifndef AFANGI_SKIL_1_CLASS
#define AFANGI_SKIL_1_CLASS

#include <iostream>

class Afangi {
public:
    //Constructors
    Afangi();
    Afangi(int id, std::string nafn, float einkunn);


    // Getters and setters
    int get_id();
    void set_id(int id);

    std::string get_nafn();
    void set_nafn(std::string nafn);

    float get_einkunn();
    void set_einkunn(float einkunn);


    // Functions
    


    // Overloads
    

private:
    int id;
    std::string nafn;
    float einkunn;
};

std::ostream& operator<<(std::ostream& ostr, Afangi& afangi);

#endif