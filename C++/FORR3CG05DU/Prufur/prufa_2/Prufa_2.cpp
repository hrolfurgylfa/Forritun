#include <iostream>
#include <string>

// using namespace std;

int main() {
    std::string input = "";
    std::cout << "Sláðu inn streng\n--->";
    std::getline(std::cin, input);
    std::cout << "Strengur: " << input << "\n";
}