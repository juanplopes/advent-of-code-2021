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
        if (f(third1) > f(third2)) 
            left = third2 + 1;
        else
            right = third1 - 1;
    }

    cout << f(left) << endl;
}