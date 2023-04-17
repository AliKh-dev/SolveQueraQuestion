#include <iostream>
using namespace std;
int main()
{
    int a[5]{'a', 'o', 'e', 'i', 'u'}, cnt_vowels = 0;
    string str;
    cin >> str;
    for (int i = 0; i < str.length(); i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (str[i] == a[j])
            {
                cnt_vowels++;
                break;
            }
        }
    }

    cout << cnt_vowels;
}