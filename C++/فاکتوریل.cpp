#include <iostream>
using namespace std;
int main()
{
    int n, result = 1;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        result = result * i;
    }
    cout << result;
}
