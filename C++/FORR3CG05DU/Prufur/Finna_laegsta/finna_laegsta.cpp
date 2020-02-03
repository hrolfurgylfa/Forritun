#include <iostream>
#include <string>

int finna_laegsta(int* fylki, int n) {
    int laegsta = *fylki;

    for (int i = 1; i < n; i++) {
        fylki++;
        if (*fylki < laegsta) laegsta = *fylki;
    }
    
    return laegsta;
}

int finna_haesta(int* fylki, int n) {
    int haesta = *fylki;

    for (int i = 1; i < n; i++) {
        fylki++;
        if (*fylki > haesta) haesta = *fylki;
    }
    
    return haesta;
}


int main() {
    int vector[] = {1, -4, -2, 8, 14, -7, 3, 9, 0};
    int n = sizeof(vector) / sizeof(vector[0]);

    std::cout << "Lægsta: " << finna_laegsta(vector, n) << "\n" << std::flush;
    std::cout << "Hæsta: " << finna_haesta(vector, n) << "\n" << std::flush;

	return 0;
}