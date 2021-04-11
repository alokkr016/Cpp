#include<bits/stdc++.h>

using namespace std;

int maxCities(vector<vector<char>> &a, int n, int m);

// Driver code to test above functions

int main()

{

   

   int t;

   cin >> t;

   while(t--)

   {

       int n, m;

       cin >> n >> m;

       vector<vector<char>> a(n, vector<char>(m));

       for (int i = 0; i < n; ++i)

       {

           for (int j = 0; j < m; ++j)

           {

               cin >> a[i][j];

           }

       }

       cout << maxCities(a, n, m) << "\n";

   }

   return 0;

}// } Driver Code Ends

int maxCities(vector<vector<char>> &s, int n, int m)

{

   // Your code goes here

int a[n][m];

memset(a, 0, sizeof(a));

for(int i = 0; i < n; i++)

{

 for(int j = 0; j < m; j++)

 {

  if(s[i][j] == '*')

  {

   if(i-1 >= 0 && j-1 >= 0 && s[i-1][j-1] == '.')

    a[i-1][j-1] = 1;

   if(i-1 >= 0 && j >= 0 && s[i-1][j] == '.')

    a[i-1][j] = 1;

   if(i-1 >= 0 && j+1 < m && s[i-1][j+1] == '.')

    a[i-1][j+1] = 1;

   if(i+1 < n && j-1 >= 0 && s[i+1][j-1] == '.')

    a[i+1][j-1] = 1;

   if(i+1 < n && j >= 0 && s[i+1][j] == '.')

    a[i+1][j] = 1;

   if(i+1 < n && j+1 < m && s[i+1][j+1] == '.')

    a[i+1][j+1] = 1;

   if(j-1 >= 0 && s[i][j-1] == '.')

    a[i][j-1] = 1;

   if(j+1 < m && s[i][j+1] == '.')

    a[i][j+1] = 1;

  }

 }

}

int vis[n][m];

memset(vis, 0, sizeof(vis));

int ans = 0;

for(int i = 0; i < n; i++)

{

 for(int j = 0; j < m; j++)

 {

  if(vis[i][j])

   continue;

  queue<pair<int,int>> q;

  q.push({i, j});

  int res = 0;

  while(!q.empty())

  {

   int x = q.front().first, y = q.front().second;

   q.pop();

   if(x >= 0 && x < n && y >= 0 && y < m && !vis[x][y] && a[x][y])

   {

    res++;

    vis[x][y] = 1;

    for(int xx = -1; xx <= 1; xx++)

    {

     for(int yy = -1; yy <= 1; yy++)

     {

      q.push({x+xx, y+yy});

     }

    }

   }

  }

  ans = max(ans, res);

 }

}

return ans;

}