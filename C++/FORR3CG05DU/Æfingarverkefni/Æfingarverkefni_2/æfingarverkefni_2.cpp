#include <iostream>
#include <string>

// using namespace std;

bool erBokstafur(char stafur) {
    return  (stafur >= 'a' && stafur <= 'z') ||
            (stafur >= 'A' && stafur <= 'Z');
}

std::string iHastafi(std::string strengur) {

    std::string nyrStrengur;
    char currentStafur;
    char haStafaMaski = 0b11011111; // Nota and til þess að fá hástafi

    for (size_t i = 0; i < strengur.length(); i++)
    {
        // Stilla currentStaf til þess að vera stafurinn sem er verið að lúppa í gegnum
        currentStafur = strengur[i];

        // Breyta currentStafur í hástaf ef stafurinn er bókstafur
        if (erBokstafur(currentStafur))
            currentStafur &= haStafaMaski;

        nyrStrengur += currentStafur;
    }

    // Bæta breytta eða óbreytta stafnum við í nýja strenginn
    return nyrStrengur;
}

std::string iLagstafi(std::string strengur) {

    std::string nyrStrengur;
    char currentStafur;
    char lagStafaMaski = 0b00100000; // Nota and til þess að fá lágstafi

    for (size_t i = 0; i < strengur.length(); i++)
    {
        // Stilla currentStaf til þess að vera stafurinn sem er verið að lúppa í gegnum
        currentStafur = strengur[i];

        // Breyta currentStafur í hástaf ef stafurinn er bókstafur
        if (erBokstafur(currentStafur))
            currentStafur |= lagStafaMaski;

        nyrStrengur += currentStafur;
    }

    // Bæta breytta eða óbreytta stafnum við í nýja strenginn
    return nyrStrengur;
}

std::string vixlaStafasetur(std::string strengur) {

    std::string nyrStrengur;
    char currentStafur;
    char switchMaski = 0b00100000; // Nota and til þess að skipta um hág/lágstafi

    for (size_t i = 0; i < strengur.length(); i++)
    {
        // Stilla currentStaf til þess að vera stafurinn sem er verið að lúppa í gegnum
        currentStafur = strengur[i];

        // Breyta currentStafur í hástaf ef stafurinn er bókstafur
        if (erBokstafur(currentStafur))
            currentStafur ^= switchMaski;

        nyrStrengur += currentStafur;
    }

    // Bæta breytta eða óbreytta stafnum við í nýja strenginn
    return nyrStrengur;
}

int ipToInt(int* ipListi) {
    unsigned long long int skila = 0;
    int moveValue = 32;

    for (size_t i = 0; i < 4; i++)
    {
        skila |= (*ipListi+i << moveValue);
        std::cout << "Skila value: " << skila << "\n" << std::flush;
        moveValue -= 8;
    }

    return skila;
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
        
        
        // ================================
        //  Breytur fyrir switch statement
        // ================================

        // Internal valmynd
        int val2 = 0;
        
        // Liður 1
        unsigned short int val;
        bool ispalindrome;

        // Liður 2
        std::string input_strengur;

        // Liður 3
        int ipListi[4];

        int* ipListiPtr = &ipListi[0];
        int ip;


        switch (menu_item)
        {
            case 1:// Liður 1
                std::cout << "Ýttu á 1 til þess að fá lið 1\n";
                std::cout << "Ýttu á 2 til þess að fá lið 2\n";
                std::cout << "Ýttu á 3 til þess að fá lið 3\n";
                std::cout << "-------------------->>> ";
                std::cin >> val2;
                switch (val2)
                {
                case 1:
                    /* code */
                    break;
                case 2:
                    /* code */
                    break;
                case 3:
                    std::cout << "value = ";
                    std::cin >> val;

                    // Insert your code here
                    std::cout << "Stærð: " << sizeof(val) << "\n";
                    for (long unsigned int i = 0; i < sizeof(val); i++) {
                        
                    }
                    
                    if(ispalindrome)
                        std::cout << val << " is a bitwise palindrome\n";
                    else
                        std::cout << val << " is not a bitwise palindrome\n";
                    
                    break;
                
                default:
                    break;
                }
            
            case 2:// Liður 2
                std::cout << "Sláðu inn streng\n--->";
                // cin.ignore() passar að C++ hoppi ekki bara yfir getline, þarf að vera fyrir fyrir
                // framan getline ef það er notað cin eitthverstaðar fyrir framan í forritinu.
                std::cin.ignore(); 
                std::getline(std::cin, input_strengur);
                // std::cin >> input_strengur;

                std::cout << iHastafi(input_strengur) << "\n";
                std::cout << iLagstafi(input_strengur) << "\n";
                std::cout << vixlaStafasetur(input_strengur) << "\n";

                break;
            
            case 3:// Liður 3
                
                std::cout << "Sláðu inn ip tölu með bilum á milli:\n";
                std::cin >> ipListi[0] >> ipListi[1] >> ipListi[2] >> ipListi[3];

                ip = ipToInt(ipListi);

                std::cout << "IP Adresses: " << ip << "\n";

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