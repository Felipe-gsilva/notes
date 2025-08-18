// esse codigo ta terrivel, n vai funcionar e nem ta pronto -- vai corinthians
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int f(float a) { return a; } // TODO

void Trap(double a, double b, int n, double *global_result_p) {
  double h, x, result, local_a, local_b;
  int i, local_n;
  int rank = omp_get_thread_num();
  int thread_count = omp_get_num_threads();

  h = (b - a) / n;
  local_n = n / thread_count;
  local_a = a + rank * local_n * h;
  local_b = local_a + local_n * h;
  result = (f(local_a) + f(local_b)) / 2.0;
}

int main() {
  double global_result_p = 0;
#pragma omp parallel
}
