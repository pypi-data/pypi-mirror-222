#include "mydist.h"

MyDist::MyDist(double shift) : shift_(shift) {}

double MyDist::dist(double x, double y) const { return x * x + y * y + shift_; }