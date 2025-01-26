#include <iostream>
using namespace std;

int main() {
    int num;
    cin >> num;
    double bonusPoints;

    if (num <= 100) {
        bonusPoints = 5; 
    } else if (num <= 1000) {
        bonusPoints = num * 0.20;
    } else {
        bonusPoints = num * 0.10;
    }

    if (num % 2 == 0) {
            bonusPoints++;
    } else if (num % 5 == 0) {
            bonusPoints += 2;
    }

    cout << bonusPoints << endl;
    cout << num + bonusPoints << endl;

    return 0;
}
