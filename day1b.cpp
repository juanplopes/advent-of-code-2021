#include<iostream>
using namespace std;

int main() {
    long long A, B, C, D;
    int count = 0;
    int answer = 0;
    while(cin >> A) {
        count++;

        if (count >= 4 && A+B+C > B+C+D) {
            answer++;
        }        
        D = C;
        C = B;
        B = A;
    }
    cout << answer << endl;
}