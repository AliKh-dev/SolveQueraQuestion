#include <iostream>
using namespace std;
int main()
{
    bool right{false};
    int column, row;
    cin >> row >> column;
    if (column <= 10)
    {
        right = true;
    }
    else
    {
        column = (20 - column) + 1;
    }
    row = (10 - row) + 1;
    if (right)
    {
        cout << "Right " << row << " " << column;
    }
    else
    {
        cout << "Left " << row << " " << column;
    }
}
