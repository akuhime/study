// Online C compiler to run C program online
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define N1 100000



double generator(){
    double a = (rand()%RAND_MAX)/(RAND_MAX*1.0);
    return a;
}
double generator_gauss(){ // [-6./,6.]
    double sum = 0;
        for(int j = 0; j < 12; j++){
            sum = sum + generator();
        }
        sum = sum - 6;
    return sum;
}
double generator_gauss_2(){ // [-inf./,inf.]
    double u = generator();
    double v = generator();
    v = 2*M_PI*v;
    double res = cos(v)*sqrt(-2*log(u));
    return res;
}
void full_array(double *a, int n){
    for(int i = 0; i < n; i++){
        a[i]=generator();
    }
}
void full_array_gauss(double *a, int n){
    for(int i = 0; i < n; i++){
        a[i] = generator_gauss();
    }
}
void full_array_gauss_2(double *a, int n){
    for(int i = 0; i < n; i++){
        a[i] = generator_gauss_2();
    }
}
void print_array(double *a, int n){
    for(int i = 0; i < n; i++){printf("%f ", a[i]);}
    printf("\n");
}

double average_array(double *a, int n){
    double b = 0;
    for(int i = 0; i < n; i++){
        b = b + a[i];
    }
    b = b/n;
    return b;
}
double standard_deviation_array(double *a, int n){
    double b = 0;
    double c = average_array(a, n);
    
    for(int i = 0; i < n; i++){
        //printf("a[%d] = %f ", i, a[i]);
        b = b + (a[i] - c)*(a[i] - c);
        //printf("b = %f  \n", b);
    }
    //printf("average = %f \n", c);
    b = b/(n-1);
    //printf(" b = b/(n-1) = %f", b);
    b = sqrt(b);
    //printf("dispersion = %f", b);
    return b;
}
double moment_array(double *a, int n, unsigned int k){
    double b = 0;
    double c = average_array(a, n);
    for(int i = 0; i < n; i++){
        b = b + pow((a[i] - c), k);
    }
    b = b/n;
    return b;
}
double Gamma1_array(double *a, int n){
    double b = 0;
    b = moment_array(a, n, 3)/(pow(standard_deviation_array(a, n),3));
    return b;
}
double Gamma2_array(double *a, int n){
    double b = 0;
    b = moment_array(a, n, 4)/(pow(standard_deviation_array(a, n),4)) - 3;
    return b;
}


int main() {
    int N = 6;
    unsigned int seed = 1;
    
    printf("enter length of array, type is integer \n");
    int res = scanf("%d", &N);
    if(res){printf("length of array is %d \n", N);}
    else{printf("wrong enter,  length of array is %d \n", N);}
    
    printf("enter seed for srand functon, type is integer \n");
    res = scanf("%u", &seed);
    if(res){printf("seed for srand functon is %u \n", seed);}
    else{printf("wrong enter,  seed for srand functon is %u \n", seed);}
    
    srand(seed);
    double mas[N];
    //uniform distribution
    full_array(mas, N);
    printf("uniform distribution \n");
    printf("average = %f \n",average_array(mas,N));
    printf("standard deviation = %f \n",standard_deviation_array(mas,N));
    printf("dispersion = %f \n",moment_array(mas,N,2));
    printf("Gamma1 = %f \n",Gamma1_array(mas,N));
    printf("Gamma2 = %f \n",Gamma2_array(mas,N));
    //gauss distribution
    full_array_gauss(mas, N);
    printf("gauss distribution \n");
    printf("average = %f \n",average_array(mas, N));
    printf("standard deviation = %f \n",standard_deviation_array(mas, N));
    printf("Gamma1 = %f \n",Gamma1_array(mas, N));
    printf("Gamma2 = %f \n",Gamma2_array(mas, N));
    //gauss distribution second way
    full_array_gauss_2(mas, N);
    printf("gauss distribution second way \n");
    printf("average = %f \n",average_array(mas, N));
    printf("standard deviation = %f \n",standard_deviation_array(mas, N));
    printf("Gamma1 = %f \n",Gamma1_array(mas, N));
    printf("Gamma2 = %f \n",Gamma2_array(mas, N));
    //print_array(mas, N);
    //printf("%f \n", generator());
    //printf("");
    //printf("%f \n", generator());
    
    return 0;
}