#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

int enc(int g, int p, int key, int m, int pk){
  int c1 = pow(g,key);
  c1 = c1%p;

  int g2 = pow(g,pk);
  g2 = g2%p;
  int c2 = m*(pow(g2,key));
  c2 = c2%p;
  return c1, c2;
}