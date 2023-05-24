# include <stdio.h>
int main(){
    //파일 읽어들이고 항 나눠서 폴리노미얼 스트럭트 두개에 저장
    typedef struct poly{
        float coef;
        int degree;
        struct poly * link;
    }poly;

    poly poly1,poly2;
    FILE* file=fopen("input.txt","r");
    if (file==NULL){
        return 0;
    }
    while(1){
        fgets(&poly1.coef ,4, file);
        fgets


    }
    
    //폴리너미얼 덧셈 구현(내림차순)

    //합할 폴리너미얼 정의, for(피연산자 각 항 차수 서로 비교 숫자 비교연산정의{비교 후), 덧셈연산정의(같으면 합 다르면 큰 쪽의 항은 합에 저장되고 다음 항으로 이동 비교 연산이 행해지면 양쪽 둘 다 
    // 다음칸으로 이동 연산자 한쪽이라도 끝나면 나머지는 복붙) 
    //폴리너미얼 곱셈 구현
    //첫째 폴리너미얼 기준 첫 폴리노미얼의 항에 두번째 폴리너미얼의 각 항 miltappend함수(링크 따라가며 항과 계수 나눠서 차례대로 곱한 후, 차수는 입서트 하기전에 헤드부터 따라가며 같으면->계수 더하기, 다르면->(비교하고자 하는게 더 
    // 크면 그 순간 {{insert함수}}), 더 작으면 다음걸로 넘어가서 반복, null 이면 끝에 붙이기(append함수))
    return 0;
}                                          