#include <iostream>
using namespace std;
int main()
{
    int temp;
    cin >> temp;
    if (temp < 0)
        cout << "Ice";
    if (temp > 100)
        cout << "Steam";
    if ((temp <= 100) & (temp >= 0))
        cout << "Water";
}
