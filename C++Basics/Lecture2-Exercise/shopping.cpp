#include <iostream>
#include <math.h>
#include <sstream>
#include <iomanip>
using namespace std;

int main() {
    double budget;
    int videocards, processors, rams;

    cin >> budget >> videocards >> processors >> rams;

    int videocardPrice = 250;
    int totalVideocardCost = 250 * videocards;
    double totalProcessorCost = totalVideocardCost * 0.35 * processors;
    double totalRamCost = totalVideocardCost * 0.10 * rams;
    
    double totalSum = totalVideocardCost + totalRamCost + totalProcessorCost;
    totalSum = videocards > processors ? totalSum * 0.85 : totalSum;

    double moneyDifference = abs(totalSum - budget);

    string resultString;
    if (budget >= totalSum) {
        stringstream stream;
        stream << "You have " << fixed << setprecision(2) << moneyDifference << " leva left!";
        resultString = stream.str();
    } else {
        stringstream stream;
        stream << "Not enough money! You need " << fixed << setprecision(2) << moneyDifference << " leva more!";
        resultString = stream.str();
    }

    cout << resultString << endl;

    return 0;
}
