#pragma once

#include <iostream>

using namespace std;

class Gogn {
    private:
        int id;
        int numer;
    public:
        Gogn();
        Gogn(int id, int numer);

        int getID();
        int getGogn();
        void prentaGogn();

        // Overloads
        bool operator>(Gogn& other);
        bool operator<(Gogn& other);
        bool operator>=(Gogn& other);
        bool operator<=(Gogn& other);

        bool operator==(Gogn& other);
        bool operator!=(Gogn& other);
};

std::ostream& operator<<(std::ostream& ostr, Gogn& flight);