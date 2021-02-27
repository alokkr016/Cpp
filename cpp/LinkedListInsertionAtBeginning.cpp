#include<bits/stdc++.h>
using namespace std;
struct node
{
    /* data */
    int data;
    node *next;
};
node *head;
void insertBeginning(int n){
    node *temp = new node();
    temp->data = n;
    temp->next = NULL;

    if(head == NULL){
        head = temp;

    }

    else
    {
        /* code */
        temp->next = head;
        head = temp;




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
    insertBeginning(2);
    print();
    insertBeginning(3);
    print();

    return 0;
}
