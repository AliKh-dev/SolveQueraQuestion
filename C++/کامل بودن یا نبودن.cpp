#include <iostream>
using namespace std;
int sum_divisor(int number);

int main()
{
    int num;
    cin >> num;
    if (sum_divisor(num) == num)
        cout << "YES";
    else
        cout << "NO";
}

int sum_divisor(int number)
{
    int sum = 0;
    for (int i = 1; i < number; i++)
        if (number % i == 0)
            sum += i;
    return sum;
}