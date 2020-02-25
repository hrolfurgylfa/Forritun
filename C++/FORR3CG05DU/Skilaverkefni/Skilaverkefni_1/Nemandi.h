#ifndef NEMANDI_SKIL_1_CLASS
#define NEMANDI_SKIL_1_CLASS

#include <iostream>

class Nemandi {
public:
    //Constructors
    Nemandi();
    Nemandi(int id, std::string nafn);


    // Getters and setters
    int get_id();
    void set_id(int id);

    std::string get_nafn();
    void set_nafn(std::string nafn);


    // Functions
    


    // Overloads
    

private:
    int id;
    std::string nafn;
    int* nemenda_listi;
};

std::ostream& operator<<(std::ostream& ostr, Nemandi& flight);

#endif