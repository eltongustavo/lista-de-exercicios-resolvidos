/*
Exercício 13
Tendo como dados de entrada um arquivo em Gigabytes, 
construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:

Para Megabytes: Gigabytes * 1024
Para Kilobytes: Gigabytes * 1024 * 1024
Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.
*/

#include <iostream>

using namespace std;

int main() {
    int tamanho;

    cout << "Digite o tamanho do arquivo em GigaBytes: ";
    cin >> tamanho;

    cout << "O tamanho do arquivo em MegaBytes é " << tamanho * 1024 << "MB" << endl;
    cout << "O tamanho do arquivo em MegaBytes é " << tamanho * 1024 * 1024 << "KB" << endl;
    return 0;
}