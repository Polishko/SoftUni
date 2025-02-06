#include <iostream>
using std::cout;
using std::cin;
using std::endl;
using std::ios;

int main() {
    const double NYLON_COST_PER_METER = 1.50;
    const double PAINT_COST_PER_LITER = 14.50;
    const double DILUTER_COST_PER_LITER = 5.00;

    const double EXTRA_PAINT_PERC = 10;
    const int EXTRA_NYLON = 2;
    const double PLASTIC_BAG_COST = 0.40;
    const double LABOR_COST_PERC_HOUR = 30;

    int nylonAmount;
    int paintAmount;
    int diluterAmount;
    int workHours;

    cin >> nylonAmount;
    cin >> paintAmount;
    cin >> diluterAmount;
    cin >> workHours;

    double nylonCost = (nylonAmount + EXTRA_NYLON) * NYLON_COST_PER_METER;
    double paintCost = paintAmount * ((EXTRA_PAINT_PERC + 100) / 100) * PAINT_COST_PER_LITER;
    double diluterCost = diluterAmount * DILUTER_COST_PER_LITER;

    double totalSumMaterials = nylonCost + paintCost + diluterCost + PLASTIC_BAG_COST;
    double laborCost = LABOR_COST_PERC_HOUR * totalSumMaterials / 100 * workHours;

    double finalSum = totalSumMaterials + laborCost;

    cout.setf(ios::fixed);
    cout.precision(2);

    cout << finalSum << endl;

    return 0;
}