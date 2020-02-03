#include <iostream>
#include <string>

int** gera_margfoldunartoflu() {

    int** outer_list = new int*[10];

    for (int i = 1; i <= 10; i++)
    {
        outer_list[i] = new int[10];
        //int* inner_list = new int[10];

        for (int j = 1; j <= 10; j++)
        {
            *inner_list = i * j;
            inner_list++;
        }
        *outer_list = inner_list;
        outer_list++;
    }
    
    return outer_list;
}

void prenta_margfoldunartoflu(int** margfoldunartafla) {
    
    // Insert your code here
    for(int i = 0; i < 10; i++) {
        for(int j = 0; j < 10; j++) {
            std::cout.width(4);
            std::cout << margfoldunartafla[i][j];
        }
        std::cout << "\n" << std::flush;
    }    
}


int main() {
    
    prenta_margfoldunartoflu(gera_margfoldunartoflu());
    std::cout << "Done" << "\n" << std::flush;

	return 0;
}