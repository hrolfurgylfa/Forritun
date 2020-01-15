#include <iostream>
#include <bitset>

using namespace std;

int main() {
    int menu_item = 0;

    while (menu_item != 4) {

        // Þessi for lúppa gerir línu sem er auðvelt að stjórna
        // stærðinni á strikinu sem kemur fyrir og eftir valmyndinna
        for (int i = 0; i < 50; i++) cout << "-";
        cout << endl << endl;//Þetta er til þess að gera tvö enter

        cout << "Ýttu á 1 til breyta í tvíundakerfið" << endl;
        cout << "Ýttu á 2 til breyta í áttundakerfið" << endl;
        cout << "Ýttu á 3 til breyta í sextándakerfið" << endl;
        cout << "Ýttu á 4 til þess að hætta" << endl;
        cout << "-------------------->>>";
        cin >> menu_item;//Hérna velur notandinn hvaða lið hann ætlar að fara í

        // Þessi for lúppa gerir línu sem er auðvelt að stjórna
        // stærðinni á strikinu sem kemur fyrir og eftir valmyndinna
        for (int i = 0; i < 50; i++) cout << "-";
        cout << endl << endl;//Þetta er til þess að gera tvö enter


        switch (menu_item)
        {
        case 1:// Liður 1
            int breyti_tala;
            cin >> breyti_tala;

            cout << bitset<2>(breyti_tala);
            break;
        
        case 2:// Liður 2
            /* code */
            break;
        
        case 3:// Liður 3
            /* code */
            break;
        
        case 4:// Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 4" þegar maður er að hætta í forritinu
            break;
        
        default:
            cout << "ERROR\tSláðu inn tölu á milli 1 og 4" << endl;
            break;
        }
    }

	return 0;
}