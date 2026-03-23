/*
Exercício 17
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
*/

#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
    double area;

    int quantidade_latas;
    int quantidade_galoes;

    cout << "Digite quantos metros quadrados serão pintados: ";
    cin >> area;
    area = area + (0.10 * area);

    quantidade_latas = ceil(area / 108);
    quantidade_galoes = ceil(area / (3.6 * 6));

    cout << fixed << setprecision(2);

    cout << "Apenas latas: " << quantidade_latas << " latas por R$ " << quantidade_latas * 80.0 << endl;
    cout << "Apenas galões: " << quantidade_galoes << " galões por R$ " << quantidade_galoes * 25.0 << endl;

    quantidade_latas = floor(area / 108);
    double resto = area - quantidade_latas * 108;

    if(resto != 0){
        quantidade_galoes = ceil(resto / (3.6 * 6));

        double desperdicio_galao = quantidade_galoes * 21.6 - resto;
        double desperdicio_lata = (quantidade_latas + 1) * 108 - area;

        if(desperdicio_galao > desperdicio_lata){
            quantidade_latas++;
            quantidade_galoes = 0;
        }
    }else{
        quantidade_galoes = 0;
    }
    
    cout << "Mistura de latas e galões: " << endl;
    cout << quantidade_latas << " latas por R$" << quantidade_latas * 80.0 << endl;
    cout << quantidade_galoes << " galões por R$" << quantidade_galoes * 25.0 << endl;

    return 0;
}
