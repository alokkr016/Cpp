#include<iostream>
using namespace std;
int main(){
    int p;
    int n;
    cout<<"Enter the number of the row ";
    cin>>n;
    
    for(int i = 1;i <= n;i++){
        int temp = i;
        p = temp;
        for(int j = 1;j <= i;j++){
            cout<< p <<" ";
            p++;
        }
        cout<<"\n";
    }
    return 0;
}