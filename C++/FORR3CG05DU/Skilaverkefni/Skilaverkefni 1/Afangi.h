#ifndef NEMANDI_SKIL_1_CLASS
#define NEMANDI_SKIL_1_CLASS

#include <iostream>

class Afangi {
public:
    //Constructors
    Afangi(int id, std::string nafn, float einkunn);


    // Getters and setters
    


    // Functions
    


    // Overloads
    

private:
    int id;
    std::string nafn;
    float einkunn;
};

std::ostream& operator<<(std::ostream& ostr, Afangi& flight);

#endif