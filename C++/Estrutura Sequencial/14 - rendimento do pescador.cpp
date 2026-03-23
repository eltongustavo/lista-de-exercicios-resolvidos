/*
Exercício 14
João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
*/

#include <iostream>

using namespace std;

int main() {
    double peso_peixes;
    double excedente;

    cout << "Digite quantos KG de peixe foram pescados: ";
    cin >> peso_peixes;

    excedente = peso_peixes - 50;

    if(excedente <= 0){
        cout << "Não houve excedentes, valor da multa: R$0,00" << endl; 
    }else{
        cout << "Houve um excendente de " << excedente << "KG, valor da multa: R$" << excedente*4 << endl; 
    }

    return 0;
}