// Online C compiler to run C program online
#include <stdio.h>
#include <math.h>
// the border region
double a1 = -2.; // Re
double a2 = 1.; // Re
double b1 = -1.; // Im
double b2 = 1.; // Im
// step
double h = 0.1;
// itteration
int N = 10000;

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

int compare(struct complex *p1, struct complex *p2)
{
    struct complex z1 = *p1;
    struct complex z2 = *p2;
    return ( abs_complex(z1) - abs_complex(z2)); 
}

int main() {

    int i = 0;  
    
    struct complex c = {a1, b1};
    struct complex z = {0.,0.};
    struct complex z2 = {0.,0.};
    
     while(c.y < b2){
        i = 0;
        c.x = a1;
        c.y = c.y + h;
        while(c.x < a2){ 
            i = 0; 
            c.x = c.x + h;
            z.x = 0.;
            z.y = 0.;
           // printf("c = ");
            //print(c);
            for(int j = 0; j<N; j++){
                z2 = mult(z,z);
                z = add(z2,c);
                //print(z);
                if(abs_complex(z)>2){i=1;
                    break;
                };
                
            }
            printf("%i ", i);
        }
        printf("\n");
    }

    

    return 0;
}