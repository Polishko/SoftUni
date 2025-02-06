#include <iostream>
using std::cout;
using std::cin;
using std::endl;

int main() {
    const double SNIKERS_COST_PERC = 60;
    const double EQUIPMENT_COST_PERC = 80;
    const double BASKETBALL_COST_COEFF = 0.25;
    const double ACCESSORIES_COST_COEFF= 0.2;

    int trainingCost;
    cin >> trainingCost;

    double snikersCost = SNIKERS_COST_PERC * trainingCost / 100;
    double equipmentCost = EQUIPMENT_COST_PERC * snikersCost / 100;
    double basketballCost = BASKETBALL_COST_COEFF * equipmentCost;
    double accessoriesCost = ACCESSORIES_COST_COEFF * basketballCost;

    double totalCost = trainingCost + snikersCost + equipmentCost + basketballCost + accessoriesCost;

    cout << totalCost << endl; 

    return 0;
}
