#include<iostream>
#include<string>
#include<cmath>
using namespace std;

int C[100];

int main() {
    string s;
    int count = 0, size = 0;
    while(cin >> s) {
        for(int i = 0; i < s.size(); i++) {
            C[i] += (s[i] == '1');
        }
        count++;
        size = max(size, (int)s.size());        
    }
    int gamma = 0, epsilon = 0;
    for(int i = 0; i < size; i++) {
        gamma <<= 1;
        epsilon <<= 1;
        
        gamma |= C[i] > count/2;
        epsilon |= C[i] <= count/2;
    }

    cout << gamma * epsilon << endl;
}