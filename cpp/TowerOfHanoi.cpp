
// C++ recursive function to
// solve tower of hanoi puzzle
#include <bits/stdc++.h>
using namespace std;
/*void towerOfHanoi(int n, char from_rod,char to_rod, char aux_rod)

{
    if (n == 1)
    {
        cout << "Move disk 1 from rod " << from_rod <<" to rod " << to_rod<<endl;
        return;
    }

    towerOfHanoi(n - 1, from_rod, aux_rod, to_rod);
    cout << "Move disk " << n << " from rod " << from_rod <<" to rod " << to_rod << endl;
    
    towerOfHanoi(n - 1, aux_rod, to_rod, from_rod);
}
*/ 
// Driver code
void moveDisks(int count, int needle1, int needle3, int needle2)
{
if (count > 0)
{
moveDisks(count - 1, needle1, needle2, needle3);
cout << "Move disk " << count << " from " << needle1
<< " to " << needle3 << "." << endl;
moveDisks(count - 1, needle2, needle3, needle1);
}
}


int main()
{
    int n = 4; // Number of disks
    moveDisks(n, 1, 3, 2); // A, B and C are names of rods
    return 0;
}
 