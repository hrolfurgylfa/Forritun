#pragma once

#include <iostream>

using namespace std;

class Verkefni {
    private:
        std::string lysing;
        bool er_skola;
        int mikilvaegi;

    public:
        Verkefni();
        Verkefni(Verkefni* verkefni);
        Verkefni(std::string lysing, bool er_skola, int mikilvaegi);

        // Getters og setters
        std::string get_lysing();
        bool get_er_skola();
        int get_mikilvaegi();
        int get_uniqe_mikilvaegi();

        // Önnur föll
        void prenta_verkefni();

        // Overloads
        bool operator>(Verkefni& other);
        bool operator<(Verkefni& other);
        bool operator>=(Verkefni& other);
        bool operator<=(Verkefni& other);

        bool operator==(Verkefni& other);
        bool operator!=(Verkefni& other);
};

std::ostream& operator<<(std::ostream& ostr, Verkefni& verkefni);