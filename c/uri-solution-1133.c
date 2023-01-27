#include <stdio.h>
 
int main() {
    int x, y,t=0;
        scanf("%d %d",&x,&y);
        t=x;
        if(x>y){
            x=y;
            y=t;
        }
        while(x<y){
             x++;
            if(x%5==2 || x%5==3 && x!=y){
                 printf("%d\n",x);
            }
        }
       
    return 0;
}
