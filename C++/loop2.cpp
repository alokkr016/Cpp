#include <iostream>
using namespace std;
int main(){
    

int n;
int count = 0;
    cout<<"Enter the number of the row ";
    cin>>n;
    int p;
    for(int i = 1; i <= n; i++){
        count += i;
        p = count;
        for (int j = 1; j <= i; j++)
        {
            cout << p << " ";
            p--;
        }
        cout<<"\n";
        
    }
    return 0;
}