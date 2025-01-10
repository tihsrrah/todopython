#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int N;
    scanf("%d",&N);
    
    int A[N];
    int j;
    for(j=0; j<N; j++)
    {
        scanf("%d", &A[j]);
    }
    
    int k;
    scanf("%d",&k);
    
    int i;
    scanf("%d",&i);
    
    int B[N+1];
    for(j=0; j<N; j++)
    {
        B[j]=A[j];
        if(j == i)
        {
            B[i]=k;
            break;
        }
    }
    for(j=i+1; j<N+1; j++)
    {
        B[j]=A[j-1];
    }

    for(int j = 0; j<N+1; j++)
    {
        printf("%d ", B[j]);
    }
    return 0;
}
