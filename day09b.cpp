#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

string T[100];
int N;
vector<int> V;


int dfs(int i, int j) {
    if (T[i][j] == '9' || i < 0 || j < 0 || i >= N || j >= T[i].size()) return 0;
    T[i][j] = '9';
    return 1 + dfs(i-1, j) + dfs(i, j-1) + dfs(i+1, j) + dfs(i, j+1);
}

int main() {
    while(cin >> T[N]) 
        N++;
    int answer = 0;
    for(int i=0; i<N; i++)
        for(int j=0; j<T[i].size(); j++)
            V.push_back(dfs(i, j));
    sort(V.begin(), V.end(), greater<int>());
    cout << V[0]*V[1]*V[2] << endl;
}