#include<iostream>
#include<cstring>
using namespace std;

long long T[10];

int main() {
    int temp; char comma;
    while(cin >> temp) {
        T[temp]++;
        cin >> comma;
    }
    for(int day=1; day<=256; day++) {
        long long temp = T[0];
        for(int i=0; i<9; i++)
            T[i] = T[i+1] + temp * (i == 6 || i == 8);
    }
    long long sum = 0;
    for(int i=0; i<9; i++)
        sum += T[i];
    cout << sum << endl;
}