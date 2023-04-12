// Online C compiler to run C program online
#include <stdio.h>
#include <math.h>

int isPrime(int n)
{
    if (n > 1)
    {   for (int i = 2; i < sqrt(n)+1; i++)
            {if (n % i == 0) return 0;}
        return 1;
    }
    else return 0;
}

unsigned long long int rec(int n) // recursion
{
    unsigned long long int a = 1;
    unsigned long long int b = 1;
    unsigned long long int c = 0;
    for(int i = 0; i < n - 2; i++){
        c = a + b;
        if(a<b){a = c;}
        else{b = c;}
    }
    if(n == 1 || n == 2) return 1;
    return c;
}

unsigned int ind(unsigned  long long int f) // index
{
    int i = 0;
    int condition = 0;
    while(!condition){
        i++;
        if(rec(i) > f){condition = 1;};
    }
    return i-1;
}

unsigned int prime(unsigned  long long int limit) // part4
{
    int i = 1;
    int condition = 0;
    unsigned  long long int value = 0;
    while(!condition){
        value = rec(i);
        if((isPrime(i)) || i == 4)
            {if(isPrime(value)){printf("%llu ",value);}
            }
        i++;
        if(rec(i) > limit){condition = 1;};
    }
    return 0;
}

unsigned int prime2(unsigned int n) // part5
{
    int i = 1;
    unsigned  long long int value = 0;
    while(i < n){
        value = rec(i);
        if((isPrime(i)) || i == 4)
            {if(isPrime(value)){printf("%llu ",value);}
            }
        i++;
    }
    return 0;
}

int main() {
    // part1 recursion
    for(int i = 0; i < 10; i++){
    printf("%llu ",rec(i+1));
    }
    printf("\n");
    //part1 index
    for(int i = 0; i < 10; i++){
    printf("%d ",ind(i+1));
    }
    printf("\n");
    //part2
 
    int k = 90;  // for 94 is wrong
    unsigned long long int sum = 0;
    for(int i = 0; i < k; i++){
        sum = sum + rec(i+1);
    }
    printf("part1 %llu \n",sum);
    unsigned long long int b = rec(k+2) - 1;
    printf("part2 %llu \n",b);
   
    //part3
    int j = 2;
    unsigned long long int f = 1;
    unsigned long long int sum2 = 0;
    while(f < 8000000000000){
        if(f % 2 == 0){sum2 = sum2 + f;}
        j++;
        f = rec(j);
    }
    printf("part3  %llu  \n", sum2);
    //part4 prime fibonacci
    printf("part4 ");
    unsigned long long int limit = 1000000;
    prime(limit);
    printf("\n");
    //part5
    printf("part5 ");
    unsigned int limit2 = 90;
    prime2(limit2);
    return 0;
}

