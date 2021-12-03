#include<iostream>
#include<string>
#include<cmath>
#include<vector>
using namespace std;

vector<string> X, Y, temp;

int filter(vector<string>& V, bool inverse) {
    for(int bit = 0; V.size() > 1; bit++) {
        int count = 0;
        temp.clear();
        for(int i=0; i<V.size(); i++) {
            count += V[i][bit] == '1';
        }

        char filter = (count >= (V.size()+1) / 2) ^ inverse ? '1' : '0';
        for(int i=0; i<V.size(); i++) {
            if (V[i][bit] == filter) {
                temp.push_back(V[i]);
            }
        }
        V = temp;
    }
    int answer = 0;
    for(int i = 0; i<V[0].size(); i++) {
        answer <<= 1;
        answer |= V[0][i] == '1';        
    }
    return answer;
}

int main() {
    string s;
    while(cin >> s) {
        X.push_back(s);
        Y.push_back(s);
    }

    cout << filter(X, false) * filter(Y, true) << endl;
}