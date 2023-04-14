#include <iostream>
using namespace std;
int main()
{
    int n,j=0,s;
    cin>>n;
    s=n;
    for(int i=1;i<=n;i++)
    {
        while(s>=0)
        {
            s-=i;
            j++;
        }
    }
    if(j%2==0)
       cout<<"Payin Barare";
    else
        cout<<"Bala Barare";
}
