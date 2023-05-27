#include <stdio.h>
void fct(int *arr,int n);
int main(){
    int array1[5]={1,2,3,4,5};
    int i,j;
    scanf("%d",&j);
    for(i=0;i<5;i++){
        printf("%d",array1[i]);
    }
    fct(array1,j);
    for(i=0;i<5;i++){
        printf("%d",array1[i]);
    }
    return 0;
}

void fct(int *arr,int n){
    arr[4]=n;
    
}