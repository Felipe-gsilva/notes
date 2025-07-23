#include "stdio.h"
#include "time.h"

double get_sort_execution_time(void (*fn)(int *, int), int *arr, int size) {
  clock_t start_time, end_time;
  start_time = clock();
  (*fn)(arr, size);
  end_time = clock();

  return (double)(end_time - start_time) / CLOCKS_PER_SEC;
}
