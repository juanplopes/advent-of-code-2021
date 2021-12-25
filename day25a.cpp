#include<iostream>
#include<string>
using namespace std;

string T[200];
int N=0;

bool step() {
    int count = 0;
    for(int i=N-1; i>=0; i--) {
        for(int j=T[i].size()-1; j>=0; j--) {
            if (T[i][j] == '>' && T[i][(j+1)%T[i].size()] == '.') {
                T[i][j] = 'x';
                T[i][(j+1)%T[i].size()] = 'y';
                count++;
            }
        }
    }
    
    for(int i=0; i<N; i++) {
        for(int j=0; j<T[i].size(); j++) {
            if (T[i][j] == 'x') T[i][j] = '.';
        }
    }

    for(int i=N-1; i>=0; i--) {
        for(int j=T[i].size()-1; j>=0; j--) {
            if (T[i][j] == 'v' && T[(i+1)%N][j] == '.') {
                T[i][j] = 'x';
                T[(i+1)%N][j] = 'z';
                count++;
            }
        }
    }
    
    for(int i=0; i<N; i++) {
        for(int j=0; j<T[i].size(); j++) {
            if (T[i][j] == 'x') T[i][j] = '.';
            if (T[i][j] == 'y') T[i][j] = '>';
            if (T[i][j] == 'z') T[i][j] = 'v';
        }
    }

    return count > 0;
}

int main() {
    while(cin >> T[N]) N++;
    int answer = 0;
    while(step()) {
        answer++;
        /*cout << "  " << answer << endl;
        for(int i=0; i<N; i++) {
            for(int j=0; j<T[i].size(); j++) {
                cout << T[i][j];
            }
            cout << endl;
        }*/
    }
    cout << answer+1 << endl;
}