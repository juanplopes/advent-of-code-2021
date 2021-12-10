#include<iostream>
#include<string>
#include<stack>
#include<vector>
#include<algorithm>
using namespace std;

stack<char> Q;
vector<long long> V;

int main() {
    string s;
    while(cin >> s) {
        Q = stack<char>();
        bool valid = true;
        for(int i=0; i<s.size(); i++) {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{' || s[i] == '<') {
                Q.push(s[i]);
            } else {
                if (s[i] == ')' && Q.top() != '(') { valid=false; break; }
                if (s[i] == ']' && Q.top() != '[') { valid=false; break; }
                if (s[i] == '}' && Q.top() != '{') { valid=false; break; }
                if (s[i] == '>' && Q.top() != '<') { valid=false; break; }
                Q.pop();
            }
        }
        if (!valid) continue;

        long long answer = 0;
        while(Q.size()) {
            answer *= 5;
            if (Q.top() == '(') { answer += 1; }
            if (Q.top() == '[') { answer += 2; }
            if (Q.top() == '{') { answer += 3; }
            if (Q.top() == '<') { answer += 4; }
            Q.pop();
        }
        V.push_back(answer);
    }
    nth_element(V.begin(), V.begin()+V.size()/2, V.end());
    cout << V[V.size()/2] << endl;

}