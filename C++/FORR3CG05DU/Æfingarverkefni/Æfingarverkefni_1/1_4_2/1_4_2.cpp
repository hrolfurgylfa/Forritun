#include <iostream>

using namespace std;

float sqared(float x) {
    return x * x;
}

int main() {
    cout << "Sláðu inn x\n--->";
    float x;
    cin >> x;

    float pi = 3.14159265358979323846;
    float pi2 = sqared(pi);
    float x2 = sqared(x);

    float a =           x2/
                ( pi2 * ( x2+0.5 ) );

    float b = 1 + (         x2/
                ( pi2 * sqared(x2-0.5) ) );

    float y;
    y = a * b;

    cout << "y: " << y << endl;
}