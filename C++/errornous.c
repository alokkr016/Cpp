#include<stdio.h>

int main()
{
  int n;
  scanf("%d", &n);
 unsigned int i = n;
  while(i >= 0)
  {
       printf("%d ", i);
       i--;
  }
 return 0;
}