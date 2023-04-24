#include <iostream>
using namespace std;
int main()
{
    bool is_in = false;
    int array[5]{0};
    for (int i = 0; i < 5; i++)
    {
        string registration_code;
        cin >> registration_code;
        for (int j = 0; j < registration_code.length() - 2; j++)
        {
            if (registration_code[j] == 'F' &&
                registration_code[j + 1] == 'B' &&
                registration_code[j + 2] == 'I')
            {
                array[i] = i + 1;
                is_in = true;
            }
        }
    }
    if (!is_in)
        cout << "HE GOT AWAY!";
    else
    {
        for (int i = 0; i < 5; i++)
        {
            if (array[i] != 0)
                cout << array[i] << " ";
        }
    }
}