#include<stdio.h>
int factorial(int);
int main()
{
   int number, fact;

   printf("Enter a number:");
   scanf("%d",&number);
 
   fact =factorial(number);
 
   printf("Factorial of %d is: %d",number,fact);   
   return 0;
}
int factorial(int n)
{
   if(n==0)
      return(1);
 
   return(n*factorial(n-1));
}