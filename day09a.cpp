#include<iostream>
#include<string>
using namespace std;

string T[100];

int main() {
    int N = 0;
    while(cin >> T[N]) 
        N++;
    int answer = 0;
    for(int i=0; i<N; i++) {
        for(int j=0; j<T[i].size(); j++) {
            if (i-1 >= 0 && T[i][j] >= T[i-1][j]) continue;
            if (j-1 >= 0 && T[i][j] >= T[i][j-1]) continue;
            if (i+1 < N && T[i][j] >= T[i+1][j]) continue;
            if (j+1 < T[i].size() && T[i][j] >= T[i][j+1]) continue;
            answer += T[i][j]-'0'+1;
        }
    }
    cout << answer << endl;
}