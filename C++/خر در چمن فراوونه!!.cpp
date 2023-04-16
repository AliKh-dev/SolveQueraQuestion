#include <iostream>
using namespace std;
int main()
{
    int a, b, l, k{0}, sum{0};
    cin >> a >> b >> l;
    while (k < l)
    {
        sum += a;
        k++;
        if (k == l)
        {
            break;
        }
        sum += b;
        k++;
    }
    cout << sum;
}
