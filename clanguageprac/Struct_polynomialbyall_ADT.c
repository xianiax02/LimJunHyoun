#include <stdio.h>


    
int main(){
        int j;
        typedef struct poly{
            int degree;
            scanf("%d\n",&degree);
            float coef[degree];
            for(j=0;j<degree;j++){
                scanf("%f",&coef[i]);
            }
        }

        poly add(poly p, poly q, *poly c){
            c->degree=(p.degree > q.degree) ? p.degree : q.degree;
            int i=0;
            for(;i<(p.degree < q.degree) ? p.degree : q.degree;){
                c->coef[i++]=p.coef[i++]+q.coef[i++];
                p.degree--;
                q.degree--;}
            while(p.degree==0&&q.degree!=0){
                c->coef[i++]=q.coef[i++];
            }
            while(p.degree!=0&&q.degree==0){
                c->coef[i++]=p.coef[i++];
            }
            }
        poly subtract(poly p, poly q, *poly c){
            // i=max(p.degree,q.degree);
            // for(;p.coef[i--]==q.coef[i--];){
            //     c->degree=i--;
            // 
            c->degree=(p.degree > q.degree) ? p.degree : q.degree;
            int i=0;
            for(;i<(p.degree < q.degree) ? p.degree : q.degree;){
                c->coef[i++]=p.coef[i++]-q.coef[i++];
                p.degree--;
                q.degree--;
                }
            while(p.degree==0&&q.degree!=0){
                c->coef[i++]=-1*q.coef[i++];
            }
            while(p.degree!=0&&q.degree==0){
                c->coef[i++]=p.coef[i++];
            }
            
        

        }
        poly a;
        poly b;
        poly c;
        add(a,b,&c);
        printf("%d",c.degree);
        printf("%f",c.coef[0]);
        printf("%f",c.coef[1]);
        printf("%f",c.coef[2]);
        return 0;
        }
    
            
        
         
    
    




    
    //get numbers and degrees of polynomial and create ADT

    //define add, subtract, multiply


    return 0;
}
    // poly a={maxdegree,{}};

    // char compare(int a, int b){
    //     if(a<b) return '>';
    //     if(a=b) return '=';
    //     if(a<b) return '<';
    // }

    // poly add(poly *p, poly *q){
    //     poly sum;
    //     switch(compare(p->degree,q->degree))
    //     case '>': sum.degree=p->degree;
    //     for(i=0;i<=(q->degree);i++){
    //         sum.coef[i]=p->coef[i]+q->coef[i];
    //     }
    //     for (i=(q->degree+1);i<=sum.degree;i++){
    //         sum.coef[i]=q->coef[i];
    //     }
    //     break;
    //     case '=': sum.degree=p->degree; 
    //     for(i=0;i<=sum.degree;i++){
    //         sum.coef[i]=p->coef[i]+q->coef[i];
    //     }
    //     break;
    //     case '<': sum.degree=q->degree; break;
    //     int i;
        
    //     return sum;
    // }

    // poly subtract(poly *p, poly *q){
    //     int i;
    //     poly sub;
    //     for(i=0;i<=degree;i++){
    //         sum.coef[i]=p->coef[i]+q->coef[i];
    //     }
    //     return sum;
    // }