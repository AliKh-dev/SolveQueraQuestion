#include <iostream>
using namespace std;
int main()
{
    int numbers[1001]{}, cnt = 0;
    while (true)
    {
        int number;
        cin >> number;
        if (number == 0)
            break;
        numbers[cnt] = number;
        cnt++;
    }
    for (int i = cnt - 1; i >= 0; i--)
    {
        cout << numbers[i] << endl;
    }
}
