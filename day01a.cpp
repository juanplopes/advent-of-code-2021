#include<iostream>
using namespace std;

int main() {
    long long A, B = 1000000000000000;
    int answer = 0;
    while(cin >> A) {
        if (A > B) {
            answer++;
        }        
        B = A;
    }
    cout << answer << endl;

}