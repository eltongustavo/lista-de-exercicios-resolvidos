/*
Exercício 09
Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

Formula
C = 5 * ((F-32) / 9).
*/

#include <iostream>

using namespace std;

int main() {
    double temperatura_fahrenheit;
    double temperatura_celsius;

    cout << "Digite a temperatura em Fahrenheit: ";
    cin >> temperatura_fahrenheit;

    temperatura_celsius = 5 * ((temperatura_fahrenheit-32) / 9);

    cout << temperatura_fahrenheit << "F° = " << temperatura_celsius << "Cº" << endl;
    return 0;
}