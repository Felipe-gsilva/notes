#include "stdbool.h"

bool containsDuplicate(int *nums, int numsSize) {
  int number = 0, range = 0;

  for (int i = 0; i < numsSize; i++) {
    number ^= nums[i];
    range ^= i;
  }

  return (number ^ range);
}
