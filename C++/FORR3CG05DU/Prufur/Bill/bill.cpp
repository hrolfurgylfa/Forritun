#include <iostream>
#include <string>

class Bill {
    private:
        int id;
        std::string tegund;
        std::string litur;
    public:
    
        // Constructors
        Bill() {
            id = 0;
            tegund = "";
            litur = "";
        }
        Bill(int id_in, std::string tegund_in, std::string litur_in) {
            id = id_in;
            tegund = tegund_in;
            litur = litur_in;
        }

        // Föll
        void Prenta() {
            std::cout << "ID: " << id << "\n" << std::flush;
            std::cout << "Tegund: " << tegund << "\n" << std::flush;
            std::cout << "Litur: " << litur << "\n" << std::flush;
        }

        // Getters og setters
};

int main() {
    Bill bill_1 = Bill(1, "Mazda", "Blár");
    Bill bill_2 = Bill(2, "", "Blár");
    Bill bill_3 = Bill();

	return 0;
}