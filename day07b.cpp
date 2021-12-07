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

int main() {
    char comma;
    while(cin >> T[N]) {
        cin >> comma;
        N++;
    }
    sort(T, T+N);
    int left = T[0], right = T[N-1];
    while(left < right) {
        int third1 = left + (right - left) / 3;
        int third2 = right - (right - left) / 3;
        int f1 = f(third1), f2 = f(third2);
        if (f1 > f2) {
            left = third2 + 1;
        } else if (f1 < f2) {
            right = third1 - 1;
        } else {
            break;
        }
    }

    cout << f(left) << endl;
}