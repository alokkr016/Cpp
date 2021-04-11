/*
Professor X wants his students to help each other in the chemistry lab. 
He suggests that every student should help out a classmate 
who scored less marks than him in chemistry and whose roll number appears after him. 
But the students are lazy and they don't want to search too far. 
They each pick the first roll number after them that fits the criteria. 
Find the marks of the classmate that each student picks. 
If a student is unable to find anyone print -1.
Note: one student may be selected by multiple classmates.

Input:
First line of input contains number of testcases T. 
For each testcase, there will be two lines, 
first of which contains N denoting the number of students in the class. 
Second line contains N space separated integers d
enoting the marks of each student roll number wise.

Output:
For each roll number, print the marks of the student he choses to help.

Your Task:
Complete the function help_classmate() that takes array containing marks and integer
 N as input parameters and returns a list of integers containing the marks of the 
 classmate that each roll number selects.
*/
#include <bits/stdc++.h> 
using namespace std; 
// } Driver Code Ends
//User function Template for C++

vector<int> help_classmate(vector<int> array, int n) 
{ 
    // code here 
    vector<int> a;
    int z,p;
    for(z = 0;z < n;z++){
        for(p = z+1;p <= n;p++){
            if(p == n || z == n - 1){
                a.push_back(-1);
                break;
            }
            if(array[z] > array[p]){
                a.push_back(array[p]);
                break;

            }

            }

        }
        return a;
    }
    
    


// { Driver Code Starts.

int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        vector<int> array(n);
        for (int i = 0; i < n; ++i)
        {
            cin>>array[i];
        }
        vector<int> result = help_classmate(array,n);
        for (int i = 0; i < n; ++i)
        {
            cout<<result[i]<<" ";
        }
        cout<<"\n";
    }
    return 0; 
}  // } Driver Code Ends