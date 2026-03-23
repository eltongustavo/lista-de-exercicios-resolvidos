/*
Exercício 04
Faça um programa que peça as 4 notas bimestrais e mostre a média.
*/

#include <iostream>

int main() {
    double nota1;
    double nota2;
    double nota3;
    double nota4;
    double media;

    std::cout << "Digite a nota 1: ";
    std::cin >> nota1;

    std::cout << "Digite a nota 2: ";
    std::cin >> nota2;

    std::cout << "Digite a nota 3: ";
    std::cin >> nota3;

    std::cout << "Digite a nota 4: ";
    std::cin >> nota4;

    media = (nota1 + nota2 + nota3 + nota4) / 4;

    std::cout << "A média das 4 notas é " << media << std::endl;
    return 0;
}