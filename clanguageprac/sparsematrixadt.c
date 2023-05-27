// # include <stdio.h>
// struct element{
//     int value;
//     int row;
//     int column;
// };
// typedef struct sparse{
//     int rows;
//     int columns;
//     int terms;
//     struct element elements[10];
// }sparse;

// sparse add(sparse a,sparse b){
//     if(a.rows!=b.columns||a.columns!=b.columns){
//         printf("크기가 같지 않습니다.");
//         break;
//     }
//     else{
//         sparse c;
//         int ca,cb,cc=0;
//         while(ca<a.terms&&cb<b.terms){
//             int inda=a.elements[ca].row*a.columns+a.rows;
//             int indb=b.elements[cb].row*b.columns+b.rows;
//             if(inda<indb){
//                 c.elements[cc++]=a.elements[ca++];
//             }

//             else if(inda==indb){
//                 if(a.elements[ca].value+b.elements[cb].value!=0){
//                     c.elements[cc].row=a.elements[ca].row;
//                     c.elements[cc].column=a.elements[ca].column;
//                     c.elements[cc++].value=a.elements[ca++].value+b.elements[cb++].value;
//                 }
//                 else{
//                     ca++;
//                     cb++;
//                 }
//             else{
//                 c.elements[cc++]=b.elements[cb++];//b의 요소가 더 앞에 있어 b 요소 그대로 베낌

//             }
//         while(ca>=a.terms&&cb<b.terms){
//               c.elements[cc++]=b.elements[cb++];
//         }
//         while(ca<a.terms&&cb>=b.terms){
//             c.elements[cc++]=a.elements[ca++];
//         }

                
//         }
//         }
//         }

//     }



// int main(){
//     sparse m1={{5,1,1},{9,2,2},3,3,2};
//     sparse m2={{5,0,0},{9,2,2},3,3,2};
//     sparse m3;
//     m3=add(m1,m2);





//     return 0;
// }
#include <stdio.h>

struct element{
    int value;
    int row;
    int column;
};

typedef struct sparse{
    int rows;
    int columns;
    int terms;
    struct element elements[10];
} sparse;

sparse add(sparse a, sparse b){
    if(a.rows != b.rows || a.columns != b.columns){
        printf("크기가 같지 않습니다.");
        return a; // 반환할 sparse matrix는 임시로 a를 사용
    }
    else{
        sparse c;
        int ca=0, cb=0, cc=0;
        while(ca < a.terms && cb < b.terms){
            int inda = a.elements[ca].row * a.columns + a.elements[ca].column;
            int indb = b.elements[cb].row * b.columns + b.elements[cb].column;
            if(inda < indb){
                c.elements[cc++] = a.elements[ca++];
            }
            else if(inda == indb){
                if(a.elements[ca].value + b.elements[cb].value != 0){
                    c.elements[cc].row = a.elements[ca].row;
                    c.elements[cc].column = a.elements[ca].column;
                    c.elements[cc++].value = a.elements[ca++].value + b.elements[cb++].value;
                }
                else{
                    ca++;
                    cb++;
                }
            }
            else{
                c.elements[cc++] = b.elements[cb++]; // b의 요소가 더 앞에 있어 b 요소 그대로 베낌
            }
        }
        while(ca < a.terms){
            c.elements[cc++] = a.elements[ca++];
        }
        while(cb < b.terms){
            c.elements[cc++] = b.elements[cb++];
        }
        c.rows = a.rows;
        c.columns = a.columns;
        c.terms = cc;
        return c;
    }
}

int main(){
    sparse m1 = {5, 5, 3, {{5, 1, 1}, {9, 2, 2}, {3, 3, 2}}};
    sparse m2 = {5, 5, 3, {{5, 0, 0}, {9, 2, 2}, {3, 3, 2}}};
    sparse m3 = add(m1, m2);

    printf("Result:\n");
    for(int i = 0; i < m3.terms; i++){
        printf("(%d, %d, %d) ", m3.elements[i].value, m3.elements[i].row, m3.elements[i].column);
    }
    printf("\n");

    return 0;
}
