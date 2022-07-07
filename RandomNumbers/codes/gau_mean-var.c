#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
//Mean
double x = mean("gau.dat");
printf("Mean = %lf\n",x);
//Variance
printf("Variance = %lf\n",mean_sqr("gau.dat")-x*x);
return 0;
}
