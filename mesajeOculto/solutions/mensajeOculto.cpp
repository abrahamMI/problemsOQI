#include "mensajeOculto.h"
#include <iostream>

void encode(int N, int M, char words[1000][1000]) {
    int test[1000];
    int idx = 0;
    for (int i = 0; i < N; i++) {
        int len = getWordLength(i);  // No redefinir M
        for (int j = 0; j < len; j++) {
            test[idx] = words[i][j]-'a';
            idx++;
        }
        test[idx++] = 100;
    }
    send(idx, test);  // Enviar incluyendo '*' y '\0'
    return;
}

void decode() {
    int N = getMessageSize();

    char ans[1000][1000]={0};

    int idx = 0;
    int i = 0;
    int hiddenMessage = getMessage(idx);

    while (idx < N) {
        int j = 0;
        int hiddenMessage = getMessage(idx);
        while (hiddenMessage != 100) {
            ans[i][j] = hiddenMessage + 'a';
            j++;
            idx++;
            hiddenMessage = getMessage(idx);
            if (idx > 10) {
                break;
            }
        }
        ans[i][j] = '\0';  // Terminar cada palabra
        idx++;  // Saltar el '*'
        i++;
    }

    verifyMessage(i, 1000, ans);  // Pasar N correcto, no 1
    return;
}

