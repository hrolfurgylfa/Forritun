#include <iostream>

#include "RadadurListi.h"

using namespace std;

int main() {

    RadadurListi listiA;
    //                 id, numer
    listiA.setjaILista(30, 40);
    listiA.setjaILista(10, 20);
    listiA.setjaILista(20, 30);
    cout << "Listi 1:" << endl;
    listiA.prentaLista();

    RadadurListi listiB = listiA;

    listiA.setjaILista(40, 0);
    cout << "Listi 2:" << endl;
    listiB.prentaLista();
    // listiB ætti ekki að innihalda 40 stakið

    // bæta við prófunum fyrir samanburðarvikjana

    
    
    return 0;
}