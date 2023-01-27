#include <stdio.h>

int main()
{
    int x, y,s=0,t=0;
    scanf("%d %d",&x,&y);
    t=x;
    if(x>y){
        x=y;
        y=t;
    }
    while(x<=y){
        if(x%13!=0){
            s=s+x;
        }
        x++;
    }
    printf("%d\n",s);
    return 0;
}
