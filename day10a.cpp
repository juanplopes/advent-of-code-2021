#include<iostream>
#include<string>
#include<stack>
using namespace std;

stack<char> Q;

int main() {
    string s;
    int answer = 0;
    while(cin >> s) {
        Q = stack<char>();
        for(int i=0; i<s.size(); i++) {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{' || s[i] == '<') {
                Q.push(s[i]);
            } else {
                if (s[i] == ')' && Q.top() != '(') { answer += 3; break; }
                if (s[i] == ']' && Q.top() != '[') { answer += 57; break; }
                if (s[i] == '}' && Q.top() != '{') { answer += 1197; break; }
                if (s[i] == '>' && Q.top() != '<') { answer += 25137; break; }
                Q.pop();
            }
        }
    }
    cout << answer << endl;

}