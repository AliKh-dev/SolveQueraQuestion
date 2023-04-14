#include <iostream>
#include <string>
using namespace std;
int main()
{
    string a;
    cin >> a;
    for (int i = 0; i < a.length(); i++)
    {
        char character = a[i];
        int number = (int)character - 48;
        cout << character << ": " << string(number, character) << endl;
    }
}
