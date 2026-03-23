/*
Exercício 16
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
*/

#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    double area;
    int quantidade_latas;

    cout << "Digite quantos metros quadrados (m²) tem a área a ser pintada: ";
    cin >> area;

    quantidade_latas = ceil(area / 54);

    cout << fixed << setprecision(2);

    cout << "São necessárias " << quantidade_latas << " de latas para pintar " << area << "m² de área" << endl;
    cout << fixed << setprecision(2) << "O que resulta em um valor final de R$" << quantidade_latas * 80.0 << endl; 
    return 0;
}