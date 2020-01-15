#include <iostream>

// using namespace std;

std::string iHastafi(std::string strengur) {

    std::string nyrStrengur;
    char currentStafur;

    for (size_t i = 0; i < strengur.length(); i++)
    {
        if (strengur[i] >= 97 && strengur[i] <= 122) {
            currentStafur = strengur[i] - 32;
            nyrStrengur += currentStafur;
        } else nyrStrengur += strengur[i];
    }

    return nyrStrengur;
}

int main() {
    int menu_item = 0;

    while (menu_item != 4) {

        // Þessi for lúppa gerir línu sem er auðvelt að stjórna
        // stærðinni á strikinu sem kemur fyrir og eftir valmyndinna
        for (int i = 0; i < 50; i++) std::cout << "-";
        std::cout << "\n\n";//Þetta er til þess að gera tvö enter

        std::cout << "Ýttu á 1 til þess að fá dæmi 1\n";
        std::cout << "Ýttu á 2 til þess að fá dæmi 2\n";
        std::cout << "Ýttu á 3 til þess að fá dæmi 3\n";
        std::cout << "Ýttu á 4 til þess að hætta\n";
        std::cout << "-------------------->>> ";
        std::cin >> menu_item;//Hérna velur notandinn hvaða lið hann ætlar að fara í

        // Þessi for lúppa gerir línu sem er auðvelt að stjórna
        // stærðinni á strikinu sem kemur fyrir og eftir valmyndinna
        for (int i = 0; i < 50; i++) std::cout << "-";
        std::cout << "\n\n";//Þetta er til þess að gera tvö enter

        std::string input_strengur;

        switch (menu_item)
        {
            case 1:// Liður 1
                /* code */
                break;
            
            case 2:// Liður 2

                std::cout << "Sláðu inn streng\n--->";
                // getline(std::cin, input_strengur);
                std::cin >> input_strengur;

                std::cout << iHastafi(input_strengur) << "\n";

                break;
            
            case 3:// Liður 3
                /* code */
                break;
            
            case 4:// Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 4" þegar maður er að hætta í forritinu
                break;
            
            default:
                std::cout << "ERROR\tSláðu inn tölu á milli 1 og 4\n";
                break;
        }
    }

	return 0;
}