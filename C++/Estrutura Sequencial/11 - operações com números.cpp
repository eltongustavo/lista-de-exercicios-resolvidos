/*
Exercício 11
Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

O produto do dobro do primeiro com metade do segundo .
A soma do triplo do primeiro com o terceiro.
O terceiro elevado ao cubo.
*/

#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int numero_inteiro1;
    int numero_inteiro2;
    double numero_real;

    cout << "Digite o primeiro número inteiro: ";
    cin >> numero_inteiro1;

    cout << "Digite o segundo número inteiro: ";
    cin >> numero_inteiro2;

    cout << "Digite o número real: ";
    cin >> numero_real;

    cout << "2x" << numero_inteiro1 << " x " << numero_inteiro2 << "/2 = " << (2 * numero_inteiro1) * (numero_inteiro2 / 2) << endl;
    cout << "3x" << numero_inteiro1 << " + " << numero_real << " = " << (3 * numero_inteiro1) + numero_real << endl;
    cout << numero_real << "^3 = " << pow(numero_real, 3) << endl; 
    return 0;
}