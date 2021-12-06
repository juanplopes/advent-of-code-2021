#include<iostream>
#include<cstring>
using namespace std;

long long T[9], N[9];

int main() {
    int temp; char comma;
    while(cin >> temp) {
        T[temp]++;
        cin >> comma;
    }
    for(int day=1; day<=256; day++) {
        memset(N, 0, sizeof N);
        N[8] += T[0];
        N[6] += T[0];
        for(int i=1; i<9; i++)
            N[i-1] += T[i];
        memcpy(T, N, sizeof N);

    }
    long long sum = 0;
    for(int i=0; i<9; i++)
        sum += T[i];
    cout << sum << endl;
}