#include <iostream>
using namespace std;

// int main() {
//     double nylonCostPerMeter = 1.50;
//     double paintCostPerLiter = 14.50;
//     double diluterCostPerLiter = 5.00;

//     double extraPaintPercent = 10;
//     int extraNylon = 2;
//     double plasticBagCost = 0.40;
//     double laborCostPercentPerHour = 30;

//     int nylonAmount;
//     int paintAmount;
//     int diluterAmount;
//     int workHours;

//     cin >> nylonAmount;
//     cin >> paintAmount;
//     cin >> diluterAmount;
//     cin >> workHours;

//     double nylonCost = (nylonAmount + extraNylon) * nylonCostPerMeter;
//     double paintCost = paintAmount * ((extraPaintPercent + 100) / 100) * paintCostPerLiter;
//     double diluterCost = diluterAmount * diluterCostPerLiter;

//     double totalSumMaterials = nylonCost + paintCost + diluterCost + plasticBagCost;
//     double laborCost = laborCostPercentPerHour * totalSumMaterials / 100 * workHours;

//     double finalSum = totalSumMaterials + laborCost;

//     cout.setf(ios::fixed);
//     cout.precision(2);

//     cout << finalSum << endl;

//     return 0;
// }