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
    
    int i;
    scanf("%d",&i);
    
    int B[N];
    for(j=0; j<N; j++)
    {
        B[j]=A[j];
        if(j==i)
        {
            break;
        }
            
    }
    for(j=i; j<N; j++)
    {
        B[j]=A[j+1];
    }
    
    for(j=0; j<N; j++)
    {
        printf("%d ",B[j]);
    }
    
    return 0;
}
