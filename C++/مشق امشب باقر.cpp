#include <iostream>
using namespace std;
int main()
{
    int n1, n2, n3;
    cin >> n1 >> n2 >> n3;
    if ((n1 <= 180) && (n1 >= 1))
        if ((n2 <= 180) && (n2 >= 1))
            if ((n3 <= 180) && (n3 >= 1))
                if (n1 + n2 + n3 == 180)
                    cout << "Yes";
                else
                    cout << "No";
            else
                cout << "No";
        else
            cout << "No";
    else
        cout << "No";
}