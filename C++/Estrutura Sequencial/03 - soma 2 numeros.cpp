/*
Exercício 03
Faça um programa que peça dois números e imprima a soma:
*/

#include <iostream>

int main() {
    int numero1;
    int numero2;

    std::cout << "Digite o primeiro número: ";
    std::cin >> numero1;

    std::cout << "Digite o primeiro número: ";
    std::cin >> numero2;

    std::cout << numero1 << " + " << numero2 << " = " << numero1 + numero2 << std::endl;
    return 0;
}