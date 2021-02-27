#include <iostream>
using namespace std;
struct node
{
    int data;
    node *next;
};

int main()
{
    node *head = NULL;
    node *temp = new node();
    temp->data = 5;
    temp->next = NULL;
    head = temp;

    temp = new node();
    temp->data = 6;
    temp->next = NULL;
    head->next = temp;

    for (node *n = head; n != NULL; n = n->next)
    {
        cout << n->data << endl;
    }
    return 0;
}