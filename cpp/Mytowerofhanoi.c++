#include<iostream>
using namespace std;

void towerOfHanoi(int n,char from,char to,char aux){
    if(n==1){
        cout<<"move disk 1 from rod "<< from <<" to rod "<<to<<endl;
        return;
    }
    towerOfHanoi(n-1,from,aux,to);
    cout<<"move disk "<<n<< " from rod "<< from <<" to rod "<<to<<endl;
    towerOfHanoi(n-1,aux,to,from);
}




int main(){
    int n = 5;
    towerOfHanoi(n,'A','C','B');
    return 0;
}