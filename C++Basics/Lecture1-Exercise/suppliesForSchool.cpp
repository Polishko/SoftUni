#include <iostream>
using namespace std;


int main() {
    double packPens = 5.80;
    double packMarkers = 7.20;
    double cleaningSolution = 1.20;

    int penCount;
    int markersCount;
    int cleanerLiters;
    double discountPercent;

    cin >> penCount;
    cin >> markersCount;
    cin >> cleanerLiters;
    cin >> discountPercent;

    double totalCost = (packPens * penCount + packMarkers * markersCount + cleaningSolution * cleanerLiters) * (100 - discountPercent) / 100;
    cout << totalCost << endl;

    return 0;
}
