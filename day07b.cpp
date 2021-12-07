#include<iostream>
#include<algorithm>
using namespace std;

int T[10000];

int main() {
    int N = 0; char comma;
    while(cin >> T[N]) {
        cin >> comma;
        N++;
    }
    sort(T, T+N);

    long long answer = 0x7f7f7f7f;
    for(int j=T[0]; j<=T[N-1]; j++) {
        long long current = 0;
        for(int i=0; i<N; i++) {
            long long x = abs(T[i] - j);
            current += x*(x+1)/2;
        }
        answer = min(answer, current);
    }
    cout << answer << endl;
}