#include<iostream>
#include<string>
using namespace std;

int main() {
    string cmd;
    int amount, x = 0, y = 0, aim = 0;
    while(cin >> cmd >> amount) {
        if (cmd == "down") aim += amount;
        if (cmd == "up") aim -= amount;
        if (cmd == "forward") {
            x += amount;
            y += aim * amount;
        }
    }
    cout << x*y << endl;
}