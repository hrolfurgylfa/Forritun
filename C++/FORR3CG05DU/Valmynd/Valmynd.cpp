#include <iostream>

// using namespace std;

int main() {
    int menu_item = 0;

    while (menu_item != 14) {

        // Þessi for lúppa gerir línu sem er auðvelt að stjórna
        // stærðinni á strikinu sem kemur fyrir og eftir valmyndinna
        for (int i = 0; i < 50; i++) std::cout << "-";
        std::cout << "\n\n";//Þetta er til þess að gera tvö enter

        std::cout << "Ýttu á 1 til þess að fá dæmi 1\n";
        std::cout << "Ýttu á 2 til þess að fá dæmi 2\n";
        std::cout << "Ýttu á 3 til þess að fá dæmi 3\n";
        std::cout << "Ýttu á 4 til þess að fá dæmi 4\n";
        std::cout << "Ýttu á 5 til þess að fá dæmi 5\n";
        std::cout << "Ýttu á 6 til þess að fá dæmi 6\n";
        std::cout << "Ýttu á 7 til þess að fá dæmi 7\n";
        std::cout << "Ýttu á 8 til þess að fá dæmi 8\n";
        std::cout << "Ýttu á 9 til þess að fá dæmi 9\n";
        std::cout << "Ýttu á 10 til þess að fá dæmi 10\n";
        std::cout << "Ýttu á 11 til þess að fá dæmi 11\n";
        std::cout << "Ýttu á 12 til þess að fá dæmi 12\n";
        std::cout << "Ýttu á 13 til þess að fá dæmi 13\n";
        std::cout << "Ýttu á 14 til þess að hætta\n";
        std::cout << "-------------------->>> ";
        std::cin >> menu_item;//Hérna velur notandinn hvaða lið hann ætlar að fara í

        // Þessi for lúppa gerir línu sem er auðvelt að stjórna
        // stærðinni á strikinu sem kemur fyrir og eftir valmyndinna
        for (int i = 0; i < 50; i++) std::cout << "-";
        std::cout << "\n\n";//Þetta er til þess að gera tvö enter


        switch (menu_item)
        {
            case 1:// Liður 1
                /* code */
                break;
            
            case 2:// Liður 2
                /* code */
                break;
            
            case 3:// Liður 3
                /* code */
                break;
            
            case 4:// Liður 4
                /* code */
                break;
            
            case 5:// Liður 5
                /* code */
                break;

            case 6:// Liður 6
                /* code */
                break;

            case 7:// Liður 7
                /* code */
                break;

            case 8:// Liður 8
                /* code */
                break;

            case 9:// Liður 9
                /* code */
                break;

            case 10:// Liður 10
                /* code */
                break;

            case 11:// Liður 11
                /* code */
                break;

            case 12:// Liður 12
                /* code */
                break;

            case 13:// Liður 13
                /* code */
                break;
            
            case 14:// Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 14" þegar maður er að hætta í forritinu
                break;
            
            default:
                std::cout << "ERROR\tSláðu inn tölu á milli 1 og 14\n";
                break;
        }
    }

	return 0;
}