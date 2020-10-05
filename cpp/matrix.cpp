#include<stdio.h>
int main ()
{
    int a[3][3],b[3][3],c[3][3],i,j;
    printf("Enter the first matrix:");
    for(i=0;i<3;i++)
    for(j=0;j<3;j++)
    scanf("%d",&a[i][j]);
    printf("Enter the second matrix:");
    for(i=0;i<3;i++)
    for(j=0;j<3;j++)
    scanf("%d",&b[i][j]);
    printf("\nThe First Matrix is:\n");
    for(i=0;i<3;i++)
    {
                    printf("\n");
                    for(j=0;j<3;j++)
                    printf("%d\t",a[i][j]);
    }
     printf("\nThe Second Matrix is:\n");
     for(i=0;i<3;i++)
     {
                     printf("\n");
                     for(j=0;j<3;j++)
                     printf("%d\t",b[i][j]);
     }                
    for(i=0;i<3;i++)
    for(j=0;j<3;j++)
    c[i][j]=a[i][j]+b[i][j];
    printf("\nThe Addition of two Matrix is\n");
    for(i=0;i<3;i++)
    {
                    printf("\n");
                    for(j=0;j<3;j++)
                    printf("%d\t",c[i][j]);
    }
    return 0;
}
