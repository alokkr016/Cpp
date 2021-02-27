#include<iostream>
using namespace std;
struct node
{
    int data;
    node *next;
};

node *head;

inserstionAtBeginning(int n){
    node *temp = new node();
    temp->data = n;
    temp->next = NULL;
    if(head == NULL){
        head = temp;
    }
    else{
        temp->next = head;
        head = temp;
    }

    

}
inserstionAtEnd(int n){
    node *temp = new node();
    temp->data = n;
    temp->next = NULL;
    if (head == NULL)
    {
        head = temp;
    }

    node *temp1 = head;
    while (temp1 == NULL)
    {
        temp1 = temp1->next;

    }
}
deletionAtBeginning(){

}
deletionAtEnd(){

}

int main()
{
    head = NULL;
    int option;
    int n;
    cout<<"what do you want to do"<<endl;
    while(1){
        cout<<"Press 1 for Insertion at begining\nPress 2 insertion at end\nPress 3 for deletion at beginging\nPress 4 for deletion end\nPress 5 for insertio at particular position";
        cin>>option;
        switch (option)
        {
        case 1:
        cout<<"Enter the number which you want to insert";
        cin>>n;
        inserstionAtBeginning(n);
            break;
        case 2:
            cout << "Enter the number which you want to insert";
            cin >> n;
            inserstionAtEnd(n);
            break;
        case 3:
            
           deletionAtBeginning();
            break;
        case 4:
            deletionAtEnd();
            break;
        case 4:
            insertionAtParticular();
            break;
        case 5:
            exit(1);
        default : 
            break;
        }

    }
}
