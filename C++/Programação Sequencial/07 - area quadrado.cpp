/*
Exercício 07
Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
*/

#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double lado;
    double area;

    cout << "Digite o lado do quadrado: ";
    cin >> lado;

    area = pow(lado, 2);

    cout << "O dobro da área do quadrado é " << area * 2 << "m²" << endl;
    return 0;
}