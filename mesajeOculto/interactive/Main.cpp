#include <iostream>
#include <string.h>
#include <cstring>
#include <vector>

#include "mensajeOculto.h"

std::vector <int> message;
std::vector<int>wordsLength;
char words[1000][1000];
int cont=0;

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
    for (int i=0;i<N;i++) {
        message.push_back(msg[i]);
    }
    return;
}

void verifyMessage(int N, int M, char decodedWords[][1000]) {
    for (int i = 0; i < N; i++) {
        if (strcmp(decodedWords[i], words[i]) != 0) {
            std::cout << cont << " " << 0;
            return;
        }
    }
    std::cout << cont << " " << 1;
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
    std::cout << message.size() << " ";
    decode();
    return 0;
}
