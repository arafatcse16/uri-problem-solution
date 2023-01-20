#include <stdio.h>
 
int main() {
    double a=3.14159, r;
    scanf("%lf",&r);
    a*=(r*r);
    printf("A=%.4f\n",a);
    return 0;
}
