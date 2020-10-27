#include <stdio.h>
int main()
{
   char s[1000], r[1000];
   int i, n, count = 0;

   printf("Input a string:\n");
   gets(s);


   while (s[count] != '\0')
      count++;

   n = count - 1;

   for (i = 0; i < count; i++) {
      r[i] = s[n];
      n--;
   }

   r[i] = '\0';

   printf("Reversed String : %s\n", r);

   return 0;
}