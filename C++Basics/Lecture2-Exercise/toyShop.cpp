#include <iostream>
#include <iomanip>
#include <sstream>
using namespace std;

int main() {
    const double puzzlePrice = 2.60;
    const int talkingDollPrice = 3;
    const double plushBearPrice= 4.10;
    const double minionPrice = 8.20;
    const int truckPrice = 2;

    const double discount = 0.25;
    const double rentPercent = 0.10;

    double tripCost;
    int puzzleCount, talkingDollCount, plushBearCount, minionCount, truckCount;
    

    cin >> tripCost >> puzzleCount >> talkingDollCount >> plushBearCount >> minionCount >> truckCount;
    int toyCount = puzzleCount + talkingDollCount + plushBearCount + minionCount + truckCount;
    double totalCost = puzzlePrice * puzzleCount + talkingDollPrice * talkingDollCount
     + plushBearPrice * plushBearCount + minionPrice * minionCount + truckPrice * truckCount; 
    
    totalCost = toyCount >=50 ? totalCost - totalCost * discount : totalCost;

    totalCost = totalCost - totalCost * rentPercent;
    double moneyDifference = abs(totalCost - tripCost);

    ostringstream stream;
    stream << fixed << setprecision(2) << moneyDifference;
    string formattedMoneyDifference = stream.str();

    cout.setf(ios::fixed);
    cout.precision(2);

    string printResult;

    if (totalCost >= tripCost) {
        printResult = "Yes! " + formattedMoneyDifference + " lv left.";
    } else {
        printResult = "Not enough money! " + formattedMoneyDifference + " lv needed.";
    }

    cout << printResult << endl;


    return 0;
}
