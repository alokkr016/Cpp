#include <iostream>
using name  

struct node
{
    int data;
    node *next;
};
node *head;

void insert(int n)
{
    node *temp = new node();
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
        cout << temp2->data;
        temp2 = temp2->next;
    }
    cout <<"\n";
}

int main()
{
    head = NULL;
    insert(5);
    insert(6);
    
    print();
    return 0;
}