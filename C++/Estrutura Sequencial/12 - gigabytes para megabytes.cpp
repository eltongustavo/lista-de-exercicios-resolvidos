/*
Exercício 12
Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula:

Formula
Gigabytes * 1024
*/

#include <iostream>

using namespace std;

int main() {
    int tamanho;

    cout << "Digite o tamanho do arquivo em GigaBytes: ";
    cin >> tamanho;

    cout << "O tamanho do arquivo em MegaBytes é " << tamanho * 1024 << "MB" << endl;
    return 0;
}