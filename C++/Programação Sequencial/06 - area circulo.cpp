/*
Exercício 06
Faça um programa que peça o raio de um círculo, calcule e mostre sua área:
*/

#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double raio;
    double area;

    cout << "Digite o raio do círculo em cm: "; 
    cin >> raio;

    area = M_PI * pow(raio, 2);

    cout << "A área do círculo de raio " << raio << "cm é " << area << "cm²" << endl;
    return 0;
}