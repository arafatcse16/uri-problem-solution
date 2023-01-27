import 'dart:io';

void main()
{
    int x,y,s=0,t=0;
    x=int.parse(stdin.readLineSync());
    y=int.parse(stdin.readLineSync());
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
    print(s);

}
