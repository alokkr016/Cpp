#include<iostream>
using namespace std;
int main(){
    int n;
    cout<<"Enter the size ";
    cin>>n;
    int nofspace = n-1;
    for(int i = 1;i <= n;i++){
        for(int space = nofspace;space > 0;space--){
            cout<<" ";
        }
        for(int j = 1;j <= i;j++){
            cout<<"*";
        }
        cout<<"\n";
        nofspace--;
        
        
    }
    return 0;
}
    
