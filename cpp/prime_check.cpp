#include <stdio.h>
int main()
{
         int i, j, n;
         printf(" Enter how many prime numbers you want to print: ");
         scanf("%d", &n);
         printf("2");

         for (i=2; i<=n; i++)
         {

                  for (j=2; j<=i; j++)
                  {
                           if(i%j == 0)
                           break;
                           else
                  {

                           printf(" %d", i);
                           break;

                  }
 
  }

         }
return 0;

}  
