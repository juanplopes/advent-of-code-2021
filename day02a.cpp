#include<iostream>
#include<string>
using namespace std;

int main() {
    string cmd;
    int amount, x = 0, y = 0;
    while(cin >> cmd >> amount) {
        if (cmd == "down") y += amount;
        if (cmd == "up") y -= amount;
        if (cmd == "forward") x += amount;
    }
    cout << x*y << endl;
}