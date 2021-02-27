#include <bits/stdc++.h>
using namespace std;
struct node
{
    int data;
    node *next;
};
node *head;

void insert(int n){
    node *temp = (node*)malloc(sizeof(struct node));
    temp->data = n;
    temp->next = NULL;
    if(head == NULL){
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
void print(){
    node *temp2 = head;
    while(temp2 != NULL){
        
        cout<<" "<<temp2->data<<"->";
        temp2 = temp2->next;
    }
    cout<<"\n";

}

int main()
{
    head = NULL;
    int n, x;
    cout << "how many number you want to enter" << endl;
    cin >> x;
    for (int i = 0; i < x; i++)
    {
        cout << "Enter the number" << endl;
        cin >> n;
        insert(n);
        print();
    }

    return 0;
}