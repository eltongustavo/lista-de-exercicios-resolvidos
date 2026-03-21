/*
Exercício 05
Faça um programa que converta metros para centímetros:
*/

#include <iostream>

int main() {
    double metros;

    std::cout << "Digite um valor em metros: ";
    std::cin >> metros;

    std::cout << metros << "m = " << metros*100 << "cm" << std::endl;
    return 0;
}