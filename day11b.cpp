#include<iostream>
#include<string>
using namespace std;

string T[10];
int N = 0;

void inc(int i, int j) {
    if (i < 0 || j < 0 || i >= N || j >= N || T[i][j] < '0') return;
    T[i][j]++;
}

int main() {
    while(cin >> T[N]) N++;

    int answer = 0;
    for(int step = 0; step < 1000; step++) {
        for(int i=0; i<N; i++) 
            for(int j=0; j<N; j++)
                T[i][j]++;

        int stepCount = 0;
        while(true) {
            int count = 0;
            for(int i=0; i<N; i++) 
                for(int j=0; j<N; j++)
                    if (T[i][j] > '9') { 
                        T[i][j] = 1;
                        count++;
                    };
            if (!count) break;
            for(int i=0; i<N; i++) 
                for(int j=0; j<N; j++)
                    if (T[i][j] == 1) { 
                        T[i][j] = 0;
                        inc(i-1, j-1); inc(i-1, j); inc(i-1, j+1);
                        inc(i, j-1);                inc(i, j+1);
                        inc(i+1, j-1); inc(i+1, j); inc(i+1, j+1);
                    };

            stepCount += count;
        }

        if (stepCount == N*N) {
            answer = step + 1;
            break;
        }

        for(int i=0; i<N; i++) 
            for(int j=0; j<N; j++)
                if (T[i][j] == 0)
                    T[i][j] = '0';
    }
    cout << answer << endl;

}