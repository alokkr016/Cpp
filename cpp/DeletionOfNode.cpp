#include <bits/stdc++.h>
using namespace std;

struct node
{
    /* data */
    int data;
    node *next;
};

node *head;

void insert(int n)
{
    
    node *temp = (node *)malloc(sizeof(struct node));
    temp->data = n;
    temp->next = NULL;
    if (head == NULL)
    {
        head = temp;
    }

    else
    {
        node *temp1 = head;

        while (temp1->next != NULL)
        {
            temp1 = temp1->next;
        }
        temp1->next = temp;
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
void fdelete(int pos){
    node *temp1 = head;
    if(pos == 1){
        head = temp1->next;
        return;
    }
    for(int i = 0;i < pos-2;i++){
        temp1 = temp1->next;
    }
    node *temp2 = temp1->next;
    temp1->next = temp2->next;
    delete temp2;

}
int main()
{
    head = NULL;
    int n;
    insert(2);
    insert(3);
    insert(8);
    insert(7);
    insert(5);
    insert(4);
    print();
    cout<<"enter the position of node which you want to delete"<<endl;
    cin>>n;
    fdelete(n);
    print();
    return 0;
}
