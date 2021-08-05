/*Write a program to produce the output as shown below:

Results:

x value y value expressions results

10      | 5        | x+=y     | x=15

10      | 5        | x-=y-2   | x=7

10      | 5        | x*=y*5  | x=250 

10      | 5        | x/=x/y   | x=5

10      | 5        | x%=y    | x=0

*/


#include<iostream>
using namespace std;

int main(){
   
    int value = 42;
    for(int i = 0;i<5;i++){
            int x = 10;
            int y = 5;
            
            cout<<"10        | 5         |x"<<char(value)<<"=y    |x="<<x + y<<endl;
            value = value + 1;
            
    }
    return 0;
}