#include <stdio.h>

int main(void) {
    int a,s1,s2,c,b,x;
    scanf("%d",&a);
    for(int i=0;i<a;i++){
    scanf("%d",&s1);
    scanf("%d",&s2);
     scanf("%d",&c);
     if(s1>s2){
    if((s1-s2)/c==0){
        printf ("0\n");
        }
        else
        b=((s1-s2)/c)+1;
        printf("%d\n",b);}
        
         else{
    if((s2-s1)/c==0){
        printf ("0\n");
        }
        else
        x=((s2-s1)/c)+1;
        printf("%d\n",x);}
        }
	return 0;
}

