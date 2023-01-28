#include <stdio.h>
 
int main() {
    int alc=0, gas=0, disl=0,n;
    printf("MUITO OBRIGADO\n");
    while(1){
        scanf("%d",&n);
        if (n==1){
            alc+=1;
        }else if( n==2){
            gas+=1;
        }else if (n==3){
            disl+=1;
        }else if (n==4){
            break;  
        }
    }
    printf("Alcool: %d\n",alc);
    printf("Gasolina: %d\n",gas);
    printf("Diesel: %d\n",disl);
 
    return 0;
}
