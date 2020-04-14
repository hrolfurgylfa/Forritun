#pragma once 

#include "GognNode.h"

class RadadurListi {
    private:
        GognNode* head;
    public:
        RadadurListi();
        void setjaILista(Gogn gogn);
        void setjaILista(int id, int numer);
        void eydaUrLista(int id);
        bool erILista(int id);
        void prentaLista();
        ~RadadurListi();

        RadadurListi(RadadurListi& gamliListinn);
        bool operator<(RadadurListi& other);
        bool operator>(RadadurListi& other);
        bool operator<=(RadadurListi& other);
        bool operator>=(RadadurListi& other);
        bool operator==(RadadurListi& other);
        bool operator!=(RadadurListi& other);
};