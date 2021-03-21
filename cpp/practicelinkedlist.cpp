#include<bits/stdc++.h>
using namespace std;
struct node{
    int data;
    node *next;
};
node *head;
void insertionbeginning(){
    int num;
    cout<<"which number you want to insert";
    cin>>num;
    node *temp = new node();
    temp->data = num;
    temp->next =NULL;
    if(head == NULL){
        head = temp;
    }
    else{
        temp->next= head;
        head = temp;
    }
    
}

void insertionatend(){
    int num; 
    cout<<"which number you want to insert";
    cin>>num;
    node *temp = new node();
    temp->data = num;
    temp->next = NULL;
    if(head == NULL){
        head = temp;
    } 
    else{
        node *temp1 = head;
        while(temp1->next != NULL){
            temp1 = temp1->next;
        }
        temp1->next = temp;


    }
}
void insertionAtAnyPosition(){
    int n,pos;
    cout<<"which number you want to insert"<<endl;
    cin>>n;
    cout<<"At what position uh want to insert\n";
    cin>>pos;
    node *temp = new node();
    temp->data = n;
    temp->next = NULL;
    if(pos == 1){
        temp->next = head;
        head = temp;
    }
    node *temp1 = head;
    for(int i = 0;i < pos - 2;i++){
        temp1 = temp1->next;

    }
    temp->next = temp1->next;
    temp1->next = temp;    
    


}
void print(){
    node *temp1 = head;
    while (temp1 != NULL)
    {

        cout << " " << temp1->data << "->";
        temp1 = temp1->next;
    }
    cout << "\n";
}



int main(){
    head = NULL;
    int choice;
    while(1){
    cout<<"what do you want to do\nPress 1 for inertion at beginning\nPress 2 for insertion at end\nPress 3 for insertion at any point\nPress 4 to display\nPress 5 to exit";
    cin>>choice;
    switch (choice)
    {
    case 1:
        insertionbeginning();
        break;
    case 2:
        insertionatend();
        break;

    case 3:
        insertionAtAnyPosition();
        break;
    case 4:
        print();
        break;
    case 5:
        exit(0);
    default:
        cout<<"No valid input";
        break;
    }
    
    
}
}
