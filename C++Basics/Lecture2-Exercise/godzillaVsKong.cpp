#include <iostream>
#include <sstream>
#include <iomanip>
#include <math.h>
using namespace std;

int main() {
    double decorCostPercent = 0.10;

    double movieBudget;
    int stuntCount;
    double dressPrice;

    cin >> movieBudget >> stuntCount >> dressPrice;

    double decorCost = movieBudget * decorCostPercent;
    double dressCost = stuntCount * dressPrice;

    dressCost = stuntCount > 150 ? dressCost - (dressCost * 0.10) : dressCost;

    double totalCost = decorCost + dressCost;
    double moneyDifference = abs(totalCost - movieBudget);

    ostringstream stream;
    stream << fixed << setprecision(2) << moneyDifference;
    string differenceString = stream.str();

    if (totalCost > movieBudget) {
        cout << "Not enough money!" << endl << "Wingard needs " << differenceString << " leva more." << endl;
    } else {
        cout << "Action!" << endl << "Wingard starts filming with " << differenceString << " leva left." << endl;
    }

    return 0;
}
