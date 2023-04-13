#include <iostream>
using namespace std;
int main()
{
    int a, b, c, temp;
    cin >> a;
    cin >> b;
    cin >> c;
    if (a < b)
    {
        temp = b;
        b = a;
        a = temp;
    }
    if (a < c)
    {
        temp = c;
        c = a;
        a = temp;
    }
    if (c * c + b * b == a * a)
        cout << "YES";
    else
        cout << "NO";
}
