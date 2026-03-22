/*
Exercício 10
Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

Formula
F = (C * 9/5) + 32
*/

#include <iostream>

using namespace std;

int main() {
    double temperatura_celsius;
    double temperatura_fahrenheit;
    
    cout << "Digite a temperatura em Celsius: ";
    cin >> temperatura_celsius;

    temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32;

    cout << temperatura_celsius<< "C° = " << temperatura_fahrenheit << "Fº" << endl;
    return 0;
}