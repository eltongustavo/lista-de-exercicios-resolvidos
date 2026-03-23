/*
Exercício 08
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.
*/

#include <iostream>

using namespace std;

int main() {
    double valor_hora;
    int horas_trabalhadas;
    double salario;

    cout << "Digite o valor da hora trabalhada: ";
    cin >> valor_hora;

    cout << "Digite quantas horas foram trabalhadas: ";
    cin >> horas_trabalhadas;

    salario = valor_hora * horas_trabalhadas;

    cout << "O valor do salário mensal é de R$" << salario << endl;
    return 0;
}