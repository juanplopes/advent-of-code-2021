#include<iostream>
#include<string>
#include<queue>
using namespace std;

string T[100];
int N;
priority_queue<int> Q;


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
            Q.push(dfs(i, j));

    int a = Q.top(); Q.pop();
    int b = Q.top(); Q.pop();
    int c = Q.top(); Q.pop();

    cout << a*b*c << endl;
}