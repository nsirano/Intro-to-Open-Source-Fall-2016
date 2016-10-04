#include <stdio.h>
#include "MathFunctions.h"

// A hack square root calculation using simple operations
double mysqrt(double x) {
  if (x <= 0) {
    return 0;
  }

  double result;
  double delta;
  result = x;

  // Do ten iterations
  int i;
  for (i = 0; i < 10; ++i) {
    if (result <= 0) {
      result = 0.1;
    }
    delta = x - (result*result);
    result = result + 0.5*delta/result;
  }
  return result;
}
