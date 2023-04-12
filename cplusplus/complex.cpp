// Online C compiler to run C program online
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

struct complex{
    double x;
    double y;
};

void print(struct complex z){
    printf("%lf + %lfi\n",z.x, z.y);
}

struct complex add(struct complex z, struct complex z2){
    struct complex res = {z.x+z2.x,z.y+z2.y};
    return res;
}

struct complex mult(struct complex z, struct complex z2){
    struct complex res = {z.x*z2.x-z.y*z2.y,z.x*z2.y+z.y*z2.x};
    return res;
}

double abs_complex(struct complex z){
    double res = sqrt(z.x*z.x + z.y*z.y);
    return res;
}

double argument(struct complex z){
    double res = atan2(z.y, z.x);
    return res;
}

struct complex conjug(struct complex z){
    struct complex res = {z.x,-z.y};
    return res;
}

void replace_conjug(struct complex *p){
    struct complex z = *p;
    *p = conjug(z);
}

int compare(const void *p1, const void *p2)
{
    struct complex *z1 = (struct complex*) p1;
    struct complex *z2 = (struct complex*) p2;
    struct complex a = *z1;
    struct complex b = *z2;
    if(((a.x*a.x + a.y*a.y) - (b.x*b.x + b.y*b.y)) > 0) return 1;
    if(((a.x*a.x + a.y*a.y) - (b.x*b.x + b.y*b.y)) == 0) return 0;
    return -1;
}

int main() {
    // Write C code here
    struct complex z = {5.,6.};
    printf("first complex number \n");
    print(z);
    printf("absolute \n");
    printf("%lf \n",abs_complex(z));
    printf("argument \n");
    printf("%lf \n",argument(z));
    printf("conjugtion \n");
    print(conjug(z));
    struct complex *p; 
    p = &z;
    replace_conjug(p);
    printf("replace z -> z* \n");
    print(z);
    struct complex z2 = {11.,-3.5};
    printf("second complex number \n");
    print(z2);
    printf("addition \n");
    print(add(z,z2));
    printf("multiplication \n");
    print(mult(z,z2));
    printf("array \n");
    struct complex mas[5] = {10.,2.,1.,1.,2.,2.,3.,1.,3.1,1.};
    for(int i = 0; i<5; i++){
        print(mas[i]);
    }
    qsort(mas, 5, sizeof(struct complex), compare);
    printf("after qsort \n");
    for(int i = 0; i<5; i++){
        print(mas[i]);
    }
    return 0;
}