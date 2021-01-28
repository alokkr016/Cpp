#include<bits/stdc++.h>
using namespace std;

struct node
{
    /* data */
    int data;
    node *next;
};

node *head;


void insert(int n, int pos){
    node *temp2 = new node();
    temp2->data = n;
    temp2->next = NULL;

    if(pos == 1){
        temp2->next = head;
        head = temp2;
        
    }
    else{
        node *temp1 = head;
        /* code */
        for(int i = 0;i  < pos - 2;i++){
            temp1 = temp1->next;
        }
        temp2->next = temp1->next;
        temp1->next = temp2;

    }
    
    



}

void print()
{
    node *temp2 = head;
    while (temp2 != NULL)
    {

        cout << " " << temp2->data << "->";
        temp2 = temp2->next;
    }
    cout << "\n";
}

int main(){
    head = NULL;
    insert(2,1);
         
    insert(3,2);
        
    insert(5,3);
        
    insert(9, 2);
       
    insert(85, 2);
       
    insert(32, 5);
        print();
    return 0;
}
