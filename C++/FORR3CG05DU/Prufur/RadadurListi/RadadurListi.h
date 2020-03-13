#pragma once 

#include "GognNode.h"

class RadadurListi {
    private:
        GognNode* head;
    public:
        RadadurListi();

        void setjaILista(int id, int numer);
        void eydaUrLista(int id);

        GognNode* finnaFyrraILista(int id);
        bool erILista(int id);

        void prentaLista();

        ~RadadurListi();
};