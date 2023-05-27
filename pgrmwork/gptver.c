#include <stdio.h>
#include <stdlib.h>

typedef struct poly {
    float coef;
    int degree;
    struct poly* link;
} poly;

poly* createNode(float coef, int degree) {
    poly* newNode = (poly*)malloc(sizeof(poly));
    if (newNode != NULL) {
        newNode->coef = coef;
        newNode->degree = degree;
        newNode->link = NULL;
    }
    return newNode;
}

void insertNode(poly** polyList, float coef, int degree) {
    poly* newNode = createNode(coef, degree);

    if (newNode != NULL) {
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
}

poly* add_poly(poly* poly1, poly* poly2) {
    poly* result = NULL;
    poly* last = NULL;

    while (poly1 != NULL && poly2 != NULL) {
        if (poly1->degree > poly2->degree) {
            if (last == NULL) {
                result = createNode(poly1->coef, poly1->degree);
                last = result;
            } else {
                last->link = createNode(poly1->coef, poly1->degree);
                last = last->link;
            }
            poly1 = poly1->link;
        } else if (poly1->degree < poly2->degree) {
            if (last == NULL) {
                result = createNode(poly2->coef, poly2->degree);
                last = result;
            } else {
                last->link = createNode(poly2->coef, poly2->degree);
                last = last->link;
            }
            poly2 = poly2->link;
        } else {
            float sum = poly1->coef + poly2->coef;
            if (sum != 0) {
                if (last == NULL) {
                    result = createNode(sum, poly1->degree);
                    last = result;
                } else {
                    last->link = createNode(sum, poly1->degree);
                    last = last->link;
                }
            }
            poly1 = poly1->link;
            poly2 = poly2->link;
        }
    }

    while (poly1 != NULL) {
        if (last == NULL) {
            result = createNode(poly1->coef, poly1->degree);
            last = result;
        } else {
            last->link = createNode(poly1->coef, poly1->degree);
            last = last->link;
        }
        poly1 = poly1->link;
    }

    while (poly2 != NULL) {
        if (last == NULL) {
            result = createNode(poly2->coef, poly2->degree);
            last = result;
        } else {
            last->link = createNode(poly2->coef, poly2->degree);
            last = last->link;
        }
        poly2 = poly2->link;
    }

    return result;
}

poly* mult_poly(poly* poly1, poly* poly2) {
    poly* result = NULL;
    poly* tmpResult = NULL;

    while (poly1 != NULL) {
        poly* term = poly2;
        poly* subresult = NULL;
        poly* last = NULL;

        while (term != NULL) {
            float coef = poly1->coef * term->coef;
            int degree = poly1->degree + term->degree;
            if (coef != 0) {
                if (last == NULL) {
                    subresult = createNode(coef, degree);
                    last = subresult;
                } else {
                    last->link = createNode(coef, degree);
                    last = last->link;
                }
            }
            term = term->link;
        }

        tmpResult = add_poly(tmpResult, subresult);
        poly1 = poly1->link;
    }

    while (tmpResult != NULL) {
        result = add_poly(result, tmpResult);
        tmpResult = tmpResult->link;
    }

    return result;
}

void free_poly(poly* polyList) {
    while (polyList != NULL) {
        poly* temp = polyList;
        polyList = polyList->link;
        free(temp);
    }
}

void print_poly(poly* polyList, FILE* file) {
    while (polyList != NULL) {
        fprintf(file, "%.1f %d\n", polyList->coef, polyList->degree);
        polyList = polyList->link;
    }
}

int main() {
    FILE* inputFile = fopen("input.txt", "r");
    FILE* outputFile = fopen("output.txt", "w");

    if (inputFile == NULL || outputFile == NULL) {
        printf("Failed to open the input or output file.\n");
        return 1;
    }

    poly* poly1 = NULL;
    poly* poly2 = NULL;

    float coef;
    int degree;
    while (fscanf(inputFile, "%f %d", &coef, &degree) == 2) {
        insertNode(&poly1, coef, degree);
        if (getc(inputFile) == '\n') {
            break;
        }
    }

    while (fscanf(inputFile, "%f %d", &coef, &degree) == 2) {
        insertNode(&poly2, coef, degree);
    }

    poly* sumResult = add_poly(poly1, poly2);
    poly* multResult = mult_poly(poly1, poly2);

    fprintf(outputFile, "Addition\n");
    print_poly(sumResult, outputFile);

    fprintf(outputFile, "Multiplication\n");
    print_poly(multResult, outputFile);

    free_poly(poly1);
    free_poly(poly2);
    free_poly(sumResult);
    free_poly(multResult);

    fclose(inputFile);
    fclose(outputFile);

    return 0;
}
