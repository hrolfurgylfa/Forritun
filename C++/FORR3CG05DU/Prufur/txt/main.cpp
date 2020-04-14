#include <iostream>
#include <string>

#include <fstream>


int main() {
    std::cout << "Forrit byrjar.\n" << std::flush;

    std::ofstream skrifaISkra("gogn.txt", std::fstream::app);
    
    if (!skrifaISkra) std::cout << "Get ekki opnað skrá." << std::flush;
    else {
        skrifaISkra << "Test" << 123 << 1.23 << "\n";
    }

    skrifaISkra.close();

    std::cout << "Forrit endar.\n" << std::flush;
    return 0;
}
