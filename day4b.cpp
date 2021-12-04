#include<iostream>
#include<string>
#include<sstream>
#include<cstring>
using namespace std;

int B[5][5], M[5][5];

int main() {
    string s; cin >> s;
    int best = 0, score; 
    while(cin >> B[0][0]) {
        memset(M, 0, sizeof M);
        for(int i=0; i<5; i++) 
            for(int j=0; j<5; j++)          
                if (i != 0 || j != 0)
                    cin >> B[i][j];

        stringstream ss(s);
        for(int count = 0, drawn; ss >> drawn; count++) {
            char comma; ss >> comma;
            for(int i=0; i<5; i++) {
                for(int j=0; j<5; j++) {
                    if (B[i][j] == drawn) {
                        M[i][j] = 1;
                        B[i][j] = 0;
                    }
                }
            }
            int win = 0, sum = 0;
            for(int i=0; i<5; i++) {
                int row = 0, column = 0;
                for(int j=0; j<5; j++) {
                    sum += B[i][j];
                    row += M[i][j];
                    column += M[j][i];
                }
                win |= row == 5 || column == 5;
            }

            if (win) {
                cout << " " << count << endl;
                if (count > best) {
                    best = count;
                    score = sum * drawn;
                }
                break;
            }
        }   
    }
    cout << score << endl;
}