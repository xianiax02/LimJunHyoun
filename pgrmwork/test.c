#include <stdio.h>
#include <stdlib.h>

typedef struct poly {
    float coef;
    int degree;
    struct poly* link;
}poly;
typedef struct subresult {
    struct poly* link;
    struct subresult* next;
}subresult;

poly* createNode(float coef, int degree) {
    poly* newNode = (poly*)malloc(sizeof(poly));
    newNode->coef = coef;
    newNode->degree = degree;
    newNode->link = NULL;
    return newNode;
}//계수, 차수를 매개변수로 노드 단위를 만들어주고 새 노드의 포인터를 반환하는 함수

void insertNode(poly** polyList, float coef, int degree) {
    poly* newNode = createNode(coef, degree);

    if (*polyList == NULL) {
        *polyList = newNode;
    //폴리리스트가 없으면 새로만든 노드의 포인터 자체를 리스트 헤드로 설정
    } else {
        poly* temp = *polyList;
        while (temp->link != NULL) {
            temp = temp->link;
        }
        temp->link = newNode;
    }
}//계수 차수 입력해서 폴리리스트에 노드를 새로 삽입해주는 함수


char compare(int a,int b){
    if(a>b){
        return('>');
    }
    else if(a==b){
        return('=');
    }
    else return('<');
}
    //합할 폴리너미얼 정의, for(피연산자 각 항 차수 서로 비교 숫자 비교연산정의{비교 후), 
    //덧셈연산정의(같으면 합 다르면 큰 쪽의 항은 합에 저장되고 다음 항으로 이동 비교 연산이 행해지면 양쪽 둘 다 
    // 다음칸으로 이동 연산자 한쪽이라도 끝나면 나머지는 복붙) 
poly* add_poly(poly* poly1,poly* poly2,poly* polysum){
    
    int a=compare(poly1->degree,poly2->degree);
    if(poly1==NULL){
        polysum->degree=poly2->degree;
        polysum->coef=poly2->coef;
        polysum->link=poly2->link;
        add_poly(poly1,poly2->link,polysum->link);  

    }
    if(poly2==NULL){
        polysum->degree=poly1->degree;
        polysum->coef=poly1->coef;
        polysum->link=poly1->link;
        add_poly(poly1->link,poly2,polysum->link);  

    }
    switch (a){
    case '>':
        polysum->degree=poly1->degree;
        polysum->coef=poly1->coef;
        add_poly(poly1->link,poly2,polysum->link);
        break;
    case '=':
        if((poly1->coef)+(poly2->coef)==0){
            add_poly(poly1->link,poly2->link,polysum->link);
        }
        else{
            polysum->degree=poly1->degree;
            polysum->coef=poly1->coef+poly2->coef;
            add_poly(poly1->link,poly2->link,polysum->link);
        }
        break;
    case '<':
        polysum->degree=poly2->degree;
        polysum->coef=poly2->coef;
        add_poly(poly1,poly2->link,polysum->link);
        break;
    
    }
    return polysum;
}
//폴리너미얼 곱셈 구현
    //첫째 폴리너미얼 기준 첫 폴리노미얼 전체를  두번째 폴리너미얼의 각 항 term으로 곱해서, (mult_each함수) subresult 다항식 연결리스트의 각 컴포넌트에 
    //그 값을 저장
    //subresult 다항식 연결리스트의 각 컴포넌트를 모두 더해서(add_poly함수 다시 사용)결과 반환
poly* mult_each(poly* poly,poly* term,poly* subresult){
    if(poly==NULL){
        return subresult;
    }
    subresult->degree=poly->degree+term->degree;
    subresult->coef=(poly->coef)*(term->coef);
    mult_each(poly->link,term,subresult->link);
    return subresult;
}
poly* mult_poly(poly* poly1,poly* poly2,poly* multpoly){
    struct subresult* subresult = malloc(sizeof(subresult));
    subresult->link = NULL;
    subresult->next = NULL;
    subresult* tmp=NULL;
    //각 텀들을 하나씩 곱한, 서브리절트라는 폴리너미얼 연결리스트를 만드는 과정
    while(poly2!=NULL){    
        tmp->link=mult_each(poly1,poly2,tmp->link);//tmp에 일시적으로 폴리1에 폴리2의 한텀을 곱한 다항식(연결리스트)의 첫 포인터를 저장
        if(poly2->link!=NULL){
            tmp->next = malloc(sizeof(subresult));
            tmp=tmp->next;
            poly2=poly2->link;//다음텀이 남아있으면, tmp는 다음 단계로 넘어가고 폴리 2도 다음텀으로 넘어간다.헤드포인터는 아직 subresult 포인터 변수에 저장
        }    
    }
    poly* result=NULL;
    result=add_poly(subresult->link,subresult->next->link,result);
    while(subresult->next->next!=NULL){
        result=add_poly(result,subresult->next->next->link,result);
        subresult=subresult->next;
    }
    return result;

}
int main() {
    //poly1, poly 2에 input.txt를 인식해 저장 완료
    FILE* file = fopen("input.txt", "r");
    poly* poly1 = NULL;
    poly* poly2 = NULL;

    float coef;
    int degree; 
    while (fscanf(file, "%f %d", &coef, &degree) == 2) {
        insertNode(&poly1, coef, degree);
        if ((getc(file) == '\n')&&(getc(file) == '\n')&&(getc(file) == '\n')) {
            break;
        }
    }

    while (fscanf(file, "%f %d", &coef, &degree) == 2) {
        insertNode(&poly2, coef, degree);
    }
    poly* polysum = (poly*)malloc(sizeof(poly));
    polysum->coef = 0;
    polysum->degree = 0;
    polysum->link = NULL;

    poly* multpoly = (poly*)malloc(sizeof(poly));
    multpoly->coef = 0;
    multpoly->degree = 0;
    multpoly->link = NULL;

    add_poly(poly1,poly2,polysum);
    mult_poly(poly1,poly2,multpoly);
    //파일 출력
    FILE* ofile = fopen("output.txt", "w");
    if (ofile == NULL) {
        printf("Failed to open the output file.\n");
        return 0;
    }

    fprintf(ofile, "Addition\n");
    while(polysum!=NULL){
        fprintf(ofile,polysum->coef);
        fprintf(ofile," ");
        fprintf(ofile,polysum->degree);
        fprintf(ofile,"\n");
        polysum=polysum->link;
    }
    fprintf(ofile, "Multiplication\n");
    while(multpoly!=NULL){
        fprintf(ofile,multpoly->coef);
        fprintf(ofile," ");
        fprintf(ofile,multpoly->degree);
        fprintf(ofile,"\n");
        multpoly=multpoly->link;
    }
    fclose(file);
    return 0;
}