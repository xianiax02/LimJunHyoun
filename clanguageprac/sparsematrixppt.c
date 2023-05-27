#define ROWS 3
#define COLS 3
#define MAX_TERMS 10
typedef struct {
    int row;
    int col;
    int value;
}element;
typedef struct SparseMatrix {
    element data[MAX_TERMS];
    int rows;
    int cols;
    int terms;
}SparseMatrix;

SparseMatrix sparse_matrix_add2(SparseMatrix a,SparseMatrix b){
    SparseMatrix c;
    int ca=0,cb=0,cc=0;
    if(a.rows!=b.rows||a.cols!=b.cols){
        fpri(stderr,"희소행렬 크기에러\n");
        exit(1);
    }
    c.rpws=a.rows;
    c.cols=a.cols;
    c.terms=0;
    while(ca<a.terms&&cb<b.terms){
        int inda=a.data[ca].rows*a.cols+a.data[ca].col;
        int indb=b.data[cb].row*b.cols+b.data[cb].col;
        if(inda<indb){
            c.data[cc++]=a.data[ca++];
        }
        else if(inda==indb){
            if
        }
    }

}