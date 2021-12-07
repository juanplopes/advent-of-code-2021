#include<iostream>
#include<algorithm>
using namespace std;

int T[10000];
int N = 0;

int f(int x) {
    int answer = 0;
    for(int i=0; i<N; i++) {
        int value = abs(T[i] - x);
        answer += (value*value+value)/2;
    }
    return answer;
}

int ternary(int left, int right) {
    while(left < right) {
        int third1 = left + (right - left) / 3;
        int third2 = right - (right - left) / 3;
        int f1 = f(third1), f2 = f(third2);
        if (f1 > f2) {
            left = third2 + 1;
        } else if (f1 < f2) {
            right = third1 - 1;
        } else {
            return f1;
        }
    }
    return f(left);
}

int main() {
    char comma;
    while(cin >> T[N]) {
        cin >> comma;
        N++;
    }
    sort(T, T+N);
    cout << ternary(T[0], T[N-1]) << endl;
}