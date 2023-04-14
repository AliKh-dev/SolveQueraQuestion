#include <iostream>
using namespace std;
int main()
{
    int n = 1, m, l = 1;
    cin >> m;
    for (int i = 1; l < m; i++)
        l = l * 2;
    cout << l;
}
