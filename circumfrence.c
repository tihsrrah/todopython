#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void push(item);
void pop();

int STK[100];
int TOP = -1, k;

int main() 
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    scanf("%d", &k);
    if(k<=1 && k>99)
    {
        return 1;
    }
    
    char s[4];
    
    while(scanf("%s", &s) != EOF)
    {
        if(strcmp(s, "push") == 0)
        {
            char item;
            scanf("%s", item);
            push(item);
        }
        else if(strcmp(s, "pop") == 0)
        {
            pop();
        }
    }
}   

void push(item)
{
    if(TOP > k-1)
    {
        printf("OF\n");
    }
    else
    {
        TOP++;
        STK[TOP]= atoi(item);
    }
}
    
void pop()
{
    int deleted;
    if(TOP == -1)
    {
        printf("UD\n");
    }
    else
    {
        deleted = STK[TOP];
        TOP--;
        printf("%d", deleted);
    }
}