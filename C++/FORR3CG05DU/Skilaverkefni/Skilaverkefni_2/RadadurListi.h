#pragma once 

#include "VerkefnaNode.h"

class RadadurListi {
    private:
        VerkefnaNode* start;
    public:
        RadadurListi();

        void append(Verkefni verkefni);
        void remove(std::string lysing);

        VerkefnaNode* find_parent(std::string lysing);
        bool contains(std::string lysing);

        void print();

        ~RadadurListi();
};