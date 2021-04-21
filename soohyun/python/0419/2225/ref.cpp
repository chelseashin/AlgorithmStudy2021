#include <stdio.h>
int d[210][210];
int main()
{
    int n,k;
    scanf("%d%d",&n,&k);
    for(int i=1;i<=k;i++)
    {
        d[0][i]=1;
    }
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=k;j++)
        {
            d[i][j]=d[i-1][j]+d[i][j-1];
        }
    }
    printf("%d",d[n][k]%1000000000);
}