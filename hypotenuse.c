#include <stdio.h>
#include <math.h>
int main(){

double AB;
double BC;
double CA;

printf("enter side AB");
scanf(" %lf" , &AB);

printf("\nenter side BC");
scanf(" %lf" , &BC);

CA =  sqrt(AB * AB + BC * BC);

printf("\nhypotenuse CA  %lf" , CA);

return 0;
}