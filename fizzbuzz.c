#include <stdio.h>
#include <string.h>
#include <math.h>
#include <assert.h>
#include <stdlib.h>
typedef unsigned int uint;

#define _GNU_SOURCE

char* answer (int *X, int *Y, int *n)
{
    if ( n%X == && n%Y == 0 )
        return "FizzBuzz\n";
    else if ( n%X == 0 ) 
        return "Fizz\n";
    else if ( n%Y == 0)
        return "Buzz\n";
    else
        return "index"; 
}

void test() {
    //printf("5,11,5");
    assert(!strcmp(answer(5,11,55),"FizzBuzz"));
    //int input2[] = {2,3,9};
    assert(!strcmp(answer(2,3,9),"Buzz"));
    //int input3[] = {5, 11, 98};
    assert(!strcmp(answer(5,11,98),98));
    printf("all test cases passed...\n");
}

void solve()
{
    int X, Y, n;
    int i;
    scanf("%d %d %d", &X, &Y, &n);
    for ( i = 1; i <= n; ++i)
    {
        char* solvd = answer(X,Y,i);
        if(strcmp(solvd,"index"))
            printf("%s\n", solvd);
        else
            printf("%d\n",i);
    }
}

int main(int argc, char* argv[]) {
    if (argc > 1 && (strncmp(argv[1], "test", 2) == 0 ))
        test();
    else
        solve();
    return
        return 0; 
}


