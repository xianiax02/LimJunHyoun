#include <stdio.h>
struct twonum {
    int first;
    int second;
};
struct twonum bubble_sort(int a,int b);
int main() {
    int i,j,n;
    scanf("%d",&n);
    int array[n];
    for(i=0;i<n;i++){
        scanf("%d",&array[i]);
    }
    for(j=1;j<n;
    j++){
        for(i=0;(i+1)<=n;i++){
        struct twonum t;
        t.first=0;
        t.second=0;
        t=bubble_sort(array[i],array[i+1]);
        array[i]=t.first;
        array[i+1]=t.second;
    }
    }
    
    for(i=0;i<n;i++){
        printf("%d,",array[i]);
    }
    return 0;
}
struct twonum bubble_sort(int a,int b){
    int tmp;
    struct twonum f;
    f.first=0;
    f.second=0;
    if(a>=b){
        tmp=a;
        a=b;
        b=tmp;
    }   
    f.first=a;
    f.second=b;
    return f;
}
