#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    string city;
    double volume;

    cin >> city >> volume;

    double rate = 0.00;
    if (volume >= 0 && volume <= 500) {
        if (city == "Sofia") {
            rate = 0.05;
        } else if (city == "Varna") {
            rate = 0.045;
        } else if (city == "Plovdiv") {
            rate = 0.055;
        }
    } else if (volume > 500 && volume <= 1000) {
        if (city == "Sofia") {
            rate = 0.07;
        } else if (city == "Varna") {
            rate = 0.075;
        } else if (city == "Plovdiv") {
            rate = 0.08;
        }   
    } else if (volume > 1000 && volume <= 10000) {
        if (city == "Sofia") {
            rate = 0.08;
        } else if (city == "Varna") {
            rate = 0.10;
        } else if (city == "Plovdiv") {
            rate = 0.12;
        }      
    } else if (volume > 10000) {
        if (city == "Sofia") {
            rate = 0.12;
        } else if (city == "Varna") {
            rate = 0.13;
        } else if (city == "Plovdiv") {
            rate = 0.145;
        }        
    }

    double commission = volume * rate;

    commission > 0 ? cout << fixed << setprecision(2) << commission : cout << "error";
    cout << endl; 

    return 0;
}
