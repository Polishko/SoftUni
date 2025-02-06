#include <iostream>
using std::cout;
using std::cin;
using std::endl;


int main() {
    const double PACK_PENS = 5.80;
    const double PACK_MARKERS = 7.20;
    const double CLEANING_SOL = 1.20;

    int penCount;
    int markersCount;
    int cleanerLiters;
    double discountPercent;

    cin >> penCount;
    cin >> markersCount;
    cin >> cleanerLiters;
    cin >> discountPercent;

    double totalCost = 
    (PACK_PENS * penCount + PACK_MARKERS * markersCount + CLEANING_SOL * cleanerLiters) * (100 - discountPercent) / 100;

    cout << totalCost << endl;

    return 0;
}
