#include <iostream>
#include <string.h>
#include <cstring>
#include <vector>

#include "mensajeOculto.h"

std::vector <int> message;
std::vector<int>wordsLength;
char words[1000][1000];
int cont=0;
bool fallo = false;

int getMessage(int i) {
    if (i>=message.size()) {
        return -1;
    }
    return message[i];
}

int getMessageSize() {
    return message.size();
}

int getWordLength(int i) {
    cont++;
    if (i>wordsLength.size()) {
        return -1;
    }
    return wordsLength[i];
}

void send(int N, int msg[1000]) {
    std::cout << "Mensaje enviado: ";
    for (int i=0;i<N;i++) {
        message.push_back(msg[i]);
        std::cout << msg[i] << " ";
    }
    std::cout << std::endl;
    return;
}

void verifyMessage(int N, int M, char decodedWords[][1000]) {
    std::cout << "******  Verificando mensaje decodificado  ****** " << std::endl;
    for (int i = 0; i < N; i++) {
        std::cout << "Recibido: " << decodedWords[i] << "\n";
        std::cout << "Original: " << words[i] << std::endl;
        if (strcmp(decodedWords[i], words[i]) != 0) {
            fallo = true;
            return;
        }
    }
    return;
}

int main() {
    int N,M;
    std::cin >> N >> M;
    for (int i=0;i<N;i++) {
        int a;
        std::cin>> a >> words[i];
        wordsLength.push_back(a);
    }
    encode(N,M,words);
    decode();
    std::cout << "Longitud del mensaje: " << message.size() << std::endl;
    std::cout << "Numero de llamadas a getWordLength: " << cont << std::endl;
    if (fallo) {
        std::cout << "Fallo en la verificacion del mensaje." << std::endl;
    } else {
        std::cout << "Mensaje verificado correctamente." << std::endl;
    }
    return 0;
}
