#include <iostream>
#include <string>

class Bill {
    private:
        int id;
        bool id_is_initialized;
        std::string tegund;
        bool tegund_is_initialized;
        std::string litur;
        bool litur_is_initialized;
    public:
    
        // Constructors
        Bill() {
            id = 0;
            id_is_initialized = false;
            tegund = "";
            tegund_is_initialized = false;
            litur = "";
            litur_is_initialized = false;
        }
        
        Bill(int id_in, std::string tegund_in, std::string litur_in) {
            id = id_in;
            id_is_initialized = true;
            tegund = tegund_in;
            tegund_is_initialized = true;
            litur = litur_in;
            litur_is_initialized = true;
        }


        // Getters og setters
        int id_get() { return id; }
        void id_set(int id_in) { id_is_initialized = true; id = id_in; }

        std::string tegund_get() { return tegund; }
        void tegund_set(std::string tegund_in) { tegund_is_initialized = true; tegund = tegund_in; }

        std::string litur_get() { return litur; }
        void litur_set(std::string litur_in) { litur_is_initialized = true; litur = litur_in; }


        // Föll
        void prenta() {
            if (id_is_initialized) { std::cout << "ID: " << id << "\n" << std::flush; }
            else { std::cout << "ID: " << "None" << "\n" << std::flush; }

            if (tegund_is_initialized) { std::cout << "Tegund: " << tegund << "\n" << std::flush; }
            else { std::cout << "Tegund: " << "None" << "\n" << std::flush; }

            if (litur_is_initialized) { std::cout << "Litur: " << litur << "\n" << std::flush; }
            else { std::cout << "Litur: " << "None" << "\n" << std::flush; }

            std::cout << "\n" << std::flush;
        }

};

int main() {
    Bill bill_1 = Bill(1, "Mazda", "Blár");
    Bill bill_2 = Bill(2, "", "Blár");
    Bill bill_3 = Bill();

    bill_1.prenta();
    bill_2.prenta();
    bill_3.prenta();

	return 0;
}