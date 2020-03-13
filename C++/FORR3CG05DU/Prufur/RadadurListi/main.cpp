#include <iostream>

#include "RadadurListi.h"

using namespace std;

int main() {
    cout << "Forrit byrjar!" << endl;

    RadadurListi listi;
    listi.setjaILista(30, 40);
    listi.setjaILista(10, 20);
    listi.setjaILista(20, 30);
    // cout << listi.finnaFyrraILista(10);
    listi.prentaLista();
    /* ætti að skrifa út:
        ID: 10, Numer: 20
        ID: 20, Numer: 30
        ID: 30, Numer: 40 */
    // cout << endl;
    // listi.eydaUrLista(10);
    // listi.prentaLista();
    /* ætti að skrifa út:
        ID: 20, Numer: 30
        ID: 30, Numer: 40 */ 
    // cout << endl;
    // listi.eydaUrLista(30);
    // listi.prentaLista();  
    /* ætti að skrifa út:
        ID: 20, Numer: 30 */ 

    return 0;
}