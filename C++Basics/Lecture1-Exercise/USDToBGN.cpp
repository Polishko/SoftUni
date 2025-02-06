#include <iostream>
using std::cout;
using std::cin;
using std::endl;
using std::ios;

int main() {
    const double CONVERSION_COEFF = 1.79549;

    double usd;
    cin >> usd;
    double bgn = usd * CONVERSION_COEFF;
    

    cout.setf(ios::fixed);
    cout.precision(2);

    cout << bgn << endl;

    return 0;
}
