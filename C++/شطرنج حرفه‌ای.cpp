#include <iostream>
using namespace std;
int main()
{
    int shah, vazir, rokh, phil, asb, sarbaz;
    cin >> shah >> vazir >> rokh >> phil >> asb >> sarbaz;
    cout << (1 - shah) << " " << (1 - vazir) << " " << (2 - rokh) << " " << (2 - phil) << " " << (2 - asb) << " " << (8 - sarbaz);
}