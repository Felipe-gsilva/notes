#include "../../utils/time-check.h"
#include "stdio.h"
#include "stdlib.h"
#include "time.h"

#define N 50000

void randomize_array(int *arr, int size, int threshold) {
  srand(time(NULL));
  for (int i = 0; i < size; i++) {
    arr[i] = rand() % threshold;
  }
}

void insertion_sort(int *arr, int size) {
  for (int i = 1; i < size; i++) {
    int k = arr[i];
    int j = i - 1;
    while (j >= 0 && arr[j] > k) {
      arr[j + 1] = arr[j];
      j -= 1;
    }
    arr[j + 1] = k;
  }
}

void print_array(int *arr, int size) {
  for (int i = 0; i < size; i++) {
    printf("%d ", arr[i]);
  }
  puts("");
}

int main() {
  int V[N];
  randomize_array(V, N, 100);
  double elapsed_time_in_s = get_sort_execution_time(insertion_sort, V, N);
  printf("Sorted Array in time elapsed: %.6fs\n", elapsed_time_in_s);
  return 0;
}
