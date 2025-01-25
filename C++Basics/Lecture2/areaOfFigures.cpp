#include <iostream>
using namespace std;

int main() {
    const double PI = 3.141592653589793;

    string figure;
    cin >> figure;

    double area;
    
    if (figure == "square") {
        double a;
        cin >> a;

        area = a * a;

    } else if (figure == "rectangle") {
        double a;
        double b;
        cin >> a;
        cin >> b;

        area = a * b;

    } else if (figure == "circle") {
        double r;
        cin >> r;

        area = r * r * PI;

    } else {
        double a;
        double b;
        cin >> a;
        cin >> b;

        area = a * b / 2;
    }

    cout.setf(ios::fixed);
    cout.precision(3);

    cout << area << endl;

    return 0;
}
