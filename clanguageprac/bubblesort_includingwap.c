#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
    int a[8];
    srand(time(0));//initiaolize random access
    int i,j;
    for(i=0;i<8;i++){
        if(i<4){
            a[i]=rand()&6+5;
        }
        else{
            a[i]=rand()&6;
        }
    
    }
    for(i=0;i<8;i++){
        printf("%d ",a[i]);
    }
    //make a sample list
    printf("\n");
    void swap(int *p, int *q){
        int tmp=*p;
        *p=*q;
        *q=tmp;    
    }
    //make a unit function swap
    for(j=0;j<8;j++){
         for(i=0;i<7;i++){
        if(a[i]>a[i+1]){
            swap(&a[i],&a[i+1]);///BEWARE OF THE IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII BECAUSE OF I+1
        }
    }
    
    //loop swap
    //make condition for lesser complexity
    }
    for(i=0;i<8;i++){
        printf("%d ",a[i]);
    }
   
}