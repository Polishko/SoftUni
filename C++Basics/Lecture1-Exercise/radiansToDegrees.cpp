#include <iostream>
#include <math.h>
using std::cout;
using std::cin;
using std::endl;

int main() {
    const int DEGREE_COEFF = 180;
    const double P = 3.14;
    
    double rad;
    cin >> rad;

    cout << round(rad * DEGREE_COEFF / P) << endl;

    return 0;
}
