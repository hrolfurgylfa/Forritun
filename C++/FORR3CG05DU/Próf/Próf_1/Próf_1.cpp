#include <iostream>
#include <string>

class Nemandi {
    private:

        int numer;
        bool vantar_numer = true;

        std::string nafn;
        bool vantar_nafn = true;

        float einkunn;
        bool vantar_einkunn = true;


    public:

          //////////////////
         // Constructors //
        //////////////////
        Nemandi() {
            
        }

        Nemandi(int numer, std::string nafn) {
            this->numer = numer;
            this->nafn = nafn;

            this->vantar_numer = false;
            this->vantar_nafn = false;
        }

        Nemandi(int numer, std::string nafn, float einkunn) {
            this->numer = numer;
            this->nafn = nafn;
            this->einkunn = einkunn;

            this->vantar_numer = false;
            this->vantar_nafn = false;
            this->vantar_einkunn = false;
        }


          ////////////////////////
         // Getters og setters //
        ////////////////////////
        
        int numer_get() { return this->numer; }
        void numer_set(int numer) { this->numer = numer; this->vantar_numer = false; }

        std::string nafn_get() { return this->nafn; }
        void nafn_set(std::string nafn) { this->nafn = nafn; this->vantar_nafn = false; }

        float einkunn_get() { return this->einkunn; }
        void einkunn_set(float einkunn) { this->einkunn = einkunn; this->vantar_einkunn = false; }


          ///////////
         // Föll //
        /////////
        
        std::string print_numer() {
            if (this->vantar_numer) {
                return "None";
            } else {
                return std::to_string(this->numer);
            }
        }

        std::string print_nafn() {
            if (this->vantar_nafn) {
                return "None";
            } else {
                return this->nafn;
            }
        }

        std::string print_einkunn() {
            if (this->vantar_einkunn) {
                return "None";
            } else {
                float rounded_einkunn = (float)((int)(this->einkunn * 100 + .5)) / 100;// Round the number

                // Remove the extra zeros that come on the end when the value is changed to a string
                std::string rounded_einkunn_str = std::to_string(rounded_einkunn);
                rounded_einkunn_str.erase( rounded_einkunn_str.find_last_not_of('0') + 1, std::string::npos );
                rounded_einkunn_str.erase ( rounded_einkunn_str.find_last_not_of('.') + 1, std::string::npos );

                return rounded_einkunn_str;
            }
        }

        void print() {
            std::cout << "Nemandi númer " << this->print_numer() << ", "
                      << this->print_nafn() << ", "
                      << "einkunn: " << this->print_einkunn()
                      << "\n" << std::flush;
        }

};

int main() {
    Nemandi nemanda_listi[] = {
        Nemandi(1, "Jón", 4.5472),
        Nemandi(2, "Kalli"),
        Nemandi(),
        Nemandi(4, "Jónína"),
        Nemandi(5, "Jóna", 6)
    };

    int length = sizeof(nemanda_listi)/sizeof(nemanda_listi[0]);
    for (int i = 0; i < length; i++)
    {
        nemanda_listi[i].print();
    }

	return 0;
}