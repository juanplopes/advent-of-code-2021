#include<iostream>
#define MAX 1000
using namespace std;

int T[MAX][MAX];

int main() {
    int x1, y1, x2, y2; char c;
    
    int answer = 0;
    while(cin >> x1 >> c >> y1 >> c >> c >> x2 >> c >> y2) {
        int xstep = (x2 > x1) - (x1 > x2);
        int ystep = (y2 > y1) - (y1 > y2);
        for(int i=x1, j=y1; i!=x2+xstep || j!=y2+ystep; i+=xstep, j+=ystep) {
            if (++T[i][j] == 2) {
                answer++;
            }
        }
    }
    
    cout << answer << endl;
}