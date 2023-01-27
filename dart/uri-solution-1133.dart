import 'dart:io';

void main()
{
    int x,y,t=0;
    x=int.parse(stdin.readLineSync());
    y=int.parse(stdin.readLineSync());
    t=x;
   if(x>y){
       x=y;
       y=t;
    }
    while(x<y){
        x++;
        if(x%5==2 || x%5==3 && x!=y){
            print(x);
        }
    }

}
