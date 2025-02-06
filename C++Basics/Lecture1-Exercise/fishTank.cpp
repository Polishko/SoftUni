#include <iostream>
#include <iostream>
using std::cout;
using std::cin;
using std::endl;

int main() {
    const double CONVERSION_FACTOR = 0.001;
    int length;
    int width;
    int height;
    double occupiedPercent;

    cin >> length;
    cin >> width;
    cin >> height;
    cin >> occupiedPercent;

    double volume = length * width * height * CONVERSION_FACTOR;
    double waterCapacity = volume * (100 - occupiedPercent) /100;

    cout << waterCapacity << endl;

    return 0;
}
