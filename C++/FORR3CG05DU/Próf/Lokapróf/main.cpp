#include <iostream>
#include <string>
#include "Stada.h"
#include "Leikmadur.h"
#include "VistarLeikmadur.h"

int main() {
    Stada austur('A', "Austur");
    Stada vestur('V', "Vestur");
    //                  id    nafn  stig stada
    VistarLeikmadur geir(101, "Geir", 0, austur);
    VistarLeikmadur konni(102, "Konni", 0, vestur);
    geir.set_stig(10);
    konni.set_stig(3);
    std::cout << geir << std::endl;
    std::cout << konni << std::endl;
    if(geir < konni) std::cout << konni.get_nafn() << " vann!\n";
    else std::cout << geir.get_nafn() << " vann!\n";
    return 0;
}