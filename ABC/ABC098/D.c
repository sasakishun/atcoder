#include<stdio.h>

int main(void){
  int n;
  int a[n];
  int xor[n];
  int sum[n];
  int count;
  int i;
  int j;
  
  scanf("%d", &n);
  count = n;
  
  for(i = 0;i<n;i++){
    scanf("%d", &a[i]);
  }
  for(i = 0;i<n;i++){
    printf("%d", a[i]);
  }
  for(j = 0;j<n-1;j++){
    xor[j] = a[j];
    sum[j] = a[j];
    for(i = j+1;i<n;i++){
      xor[i] = xor[i - 1] ^ a[i];
      sum[i] = sum[i-1] + a[i];
      if (xor[i] == sum[i]){
	count++;
      }
    }
  }
  printf("%d", count);
}
