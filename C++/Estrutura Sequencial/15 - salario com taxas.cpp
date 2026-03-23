/*
Exercício 15
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
*/

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    double valor_hora;
    int horas_trabalhadas;
    double salario_bruto;
    double imposto_renda;
    double inss;
    double sindicato;
    double salario_liquido;

    cout << "Digite o valor da hora trabalhada: R$";
    cin >> valor_hora;

    cout << "Digite quantas horas foram trabalhadas: ";
    cin >> horas_trabalhadas;

    salario_bruto = valor_hora * horas_trabalhadas;

    imposto_renda = 0.11 * salario_bruto;
    inss = 0.08 * salario_bruto;
    sindicato = 0.05 * salario_bruto;

    salario_liquido = salario_bruto - imposto_renda - inss - sindicato;

    cout << fixed << setprecision(2);

    cout << "+ Salário Bruto : R$" << salario_bruto << endl;
    cout << "- IR (11%) : R$" << imposto_renda << endl;
    cout << "- INSS (8%) : R$" << inss << endl;
    cout << "- Sindicato (5%) : R$" << sindicato << endl;
    cout << "= Salário Liquido: R$" << salario_liquido << endl;

    return 0;
}