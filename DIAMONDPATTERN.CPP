#include<stdio.h>
#include<conio.h>
int main()
{ int i,j,c=0,m=0;
 for(i=1;i<=7;i++)
 {i<=4?m++:m--;
 for(j=1;j<=7;j++)
  {if(j>=5-m && j<=3+m && c==1)
   {
     printf("*");
      c=0;
 }
 else
    printf("  ");
    c=1;
    
} 
  printf("\t");
  printf("\n");
 }
}
