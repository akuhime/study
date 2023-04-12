// Online C compiler to run C program online
#include <stdio.h>
#include <math.h>
#define pi 3.14159265358979323846


long int factorial(int n){
    long int m = 1;
    for(int i = 2; i < n+1; i++){m = m*i;};
    return m;
}

long double func(long double x){ //part1

    long double mas[8] = 
    {1./6, -1./30, 1./42, -1./30, 
    5./66, -691./2730, 7./6, -3617./510};
    long double result = 0;
    long double a = 0;
    long double sum = 0;
    if(x>9.5){
        for(int k = 1; k<9; k++){
        
           sum = sum 
           + mas[k-1]*(1/(2*k*(2*k-1)))*(1/powl(x,2*k-1));
        }
        a = (x-0.5)*logl(x) - x + 0.5*logl(2*pi) + sum;
        result = expl(a);
    }
    else {
        result = func(x+1)/x;
        
    }
    return result;
}

int main() {
    // part2
    printf("%Lf \n", func(10.)); 
    printf("%Lf \n", func(0.5));
    //part3
    printf("n  ");
    printf("n!                   ");
    printf("Gamma(n+1)                   ");
    printf("eps");
    printf("\n");
    for(int i = 1; i<21; i++){
        printf("%-2i ", i);
        printf("%-20li ", factorial(i));
        long double b = func(i+1);
        printf("%-27Lf ", b);
        printf("%-7Lf ", (b - factorial(i))/factorial(i));
        printf("\n");
    }
    //part4
    printf("  z         ");
    printf("Gamma(z)/Gamma(1-z)  ");
    printf("pi/(sin(pi*z))    ");
    printf("eps");
    printf("\n");
    long double z = 0.;
    long double e = 0.;
    for(int i = 0; i<20; i++){
        z = -0.95 + 0.1*i;
        printf("%-10Lf ", z);
        printf("%-20Lf ", func(z)/func(1-z));
        e = pi/(sin(pi*z));
        printf("%-18Lf ", e);
        printf("%-12Lf ", ((func(z)/func(1-z)) - e)/(func(z)/func(1-z)));
        printf("\n");
    }
    
    
    return 0;
}