/*
Exercício 18
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
*/

#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int tamanho_arquivo;
    int velocidade;
    int tempo;

    cout << "Digite o tamanho do arquivo em (MB): ";
    cin >> tamanho_arquivo;

    cout << "Digite a velocidade da internet em (Mbps): ";
    cin >> velocidade;

    tempo = ceil((tamanho_arquivo / velocidade) * 60);
    cout << "A tempo para realizar o download será de " << tempo << " minutos" << endl;
    return 0;
}

