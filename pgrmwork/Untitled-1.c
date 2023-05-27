#include <stdio.h>
#include <stdlib.h>

typedef struct poly {
    float coef;
    int degree;
    struct poly* link;
} poly;

poly* createNode(float coef, int degree) {
    poly* newNode = (poly*)malloc(sizeof(poly));
    newNode->coef = coef;
    newNode->degree = degree;
    newNode->link = NULL;
    return newNode;
}

void insertNode(poly** polyList, float coef, int degree) {
    poly* newNode = createNode(coef, degree);

    if (*polyList == NULL) {
        *polyList = newNode;
    } else {
        poly* temp = *polyList;
        while (temp->link != NULL) {
            temp = temp->link;
        }
        temp->link = newNode;
    }
}

void printPolynomial(poly* polyList) {
    poly* temp = polyList;
    while (temp != NULL) {
        printf("%.1f x^%d ", temp->coef, temp->degree);
        temp = temp->link;
        if (temp != NULL) {
            printf("+ ");
        }
    }
    printf("\n");
}

int main() {
    FILE* file = fopen("input.txt", "r");
    if (file == NULL) {
        printf("Failed to open the input file.\n");
        return 0;
    }

    poly* poly1 = NULL;
    poly* poly2 = NULL;
    poly** currentPoly = &poly1;

    float coef;
    int degree;

    while (fscanf(file, "%f %d", &coef, &degree) == 2) {
        insertNode(currentPoly, coef, degree);

        char nextChar = getc(file);
        if (nextChar == '\n') {
            if (*currentPoly == NULL) {
                currentPoly = &poly2;
            } else {
                break;
            }
        }
    }

    printf("Polynomial 1: ");
    printPolynomial(poly1);

    printf("Polynomial 2: ");
    printPolynomial(poly2);

    fclose(file);
    return 0;
}
