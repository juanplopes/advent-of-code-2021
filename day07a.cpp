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
    int answer = 0;
    for(int i=0; i<N; i++) {
        answer += abs(T[i] - T[N/2]);
    }
    cout << answer << endl;
}