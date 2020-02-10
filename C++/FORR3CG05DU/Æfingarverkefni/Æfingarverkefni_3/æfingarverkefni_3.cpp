#include <iostream>
#include <string>

class ShopItemOrder {
    private:
        std::string item_name;
        int unit_price;
        int count;
    public:

        /////////////////////////
        // Constructors
        /////////////////////////

        ShopItemOrder(std::string item_name, int unit_price, int count) {
            this->item_name = item_name;
            this->unit_price = unit_price;
            this->count = count;
        }


        /////////////////////////
        // Getters og setters
        /////////////////////////

        std::string get_item_name() { return this->item_name; }
        int get_unit_price() { return this->unit_price; }
        int get_count() { return this->count; }

        void set_item_name(std::string item_name) { this->item_name = item_name; }
        void set_unit_price(int unit_price) { this->unit_price = unit_price; }
        void set_count(int count) { this->count = count; }


        /////////////////////////
        // Public Föll
        /////////////////////////

        int total_price() { return this->unit_price * this->count; }
        void print() {
            std::cout << 
            "Vara: " << this->item_name << "\n" <<
            "Stikkjaverð: " << this->unit_price << "\n" <<
            "Fjöldi: " << this->count << "\n" << 
            "Heildarverð: " << this->total_price() << "\n" << std::flush;
        }
};

int main() {
    // ShopItemOrder hlutur = ShopItemOrder("Bangsi", 4500, 3);
    // hlutur.print();

    ShopItemOrder nokkrir_hlutir[] = {
        ShopItemOrder("Bangsi", 4500, 3),
        ShopItemOrder("Sími", 2495, 1),
        ShopItemOrder("Hljóðkerfi", 129900, 57)
    };

    int lengd = sizeof(nokkrir_hlutir) / sizeof(nokkrir_hlutir[0]);

    for (int i = 0; i < lengd; i++) {
        nokkrir_hlutir[i].print();
        std::cout << "\n" << std::flush;
    }

    int heildarverd = 0;
    for (int i = 0; i < lengd; i++) {
        heildarverd += nokkrir_hlutir[i].total_price();
    }
    std::cout << "Verð allra vara: " << heildarverd;

    return 0;
}