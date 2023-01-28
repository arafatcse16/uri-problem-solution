import 'dart:io';

void main()
{
    int alc=0, gas=0, disl=0,n;
    print("MUITO OBRIGADO");
    while(true){
        n=int.parse(stdin.readLineSync());
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
    print("Alcool: $alc");
    print("Gasolina: $gas");
    print("Diesel: $disl");
 
}
