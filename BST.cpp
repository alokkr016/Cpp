#include<iostream>
using namespace std;
struct BstNode{
    int data;
    BstNode *left;
    BstNode *right;
};
BstNode *get_a_newNode(int data){
    BstNode* newNode = new BstNode();
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;

}
BstNode* insert(BstNode *root,int data){
    if(root == NULL){
        root = get_a_newNode(data);
    }
    else if (data <= root->data)
    {
        root->left = 
    
        
    }
    
} 
int main(){
    BstNode *root = NULL;
    root = insert(root, 8);
    root = insert(root, 69);
    root = insert(root, 5);
}