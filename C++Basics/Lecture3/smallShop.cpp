#include <iostream>
using namespace std;

int main() {
    string product, city;
    double quantity;

    cin >> product >> city >> quantity;

    double cost;
    if (product == "coffee") {
        if (city == "Sofia") {
            cost = 0.50;
        } else if (city == "Plovdiv") {
            cost = 0.40;
        } else if (city == "Varna") {
            cost = 0.45;
        }
    } else if (product == "water") {
        if (city == "Sofia") {
            cost = 0.80;
        } else if (city == "Plovdiv") {
            cost = 0.70;
        } else if (city == "Varna") {
            cost = 0.70;
        }
    } else if (product == "beer") {
        if (city == "Sofia") {
            cost = 1.20;
        } else if (city == "Plovdiv") {
            cost = 1.15;
        } else if (city == "Varna") {
            cost = 1.10;
        }   
    } else if (product == "sweets") {
        if (city == "Sofia") {
            cost = 1.45;
        } else if (city == "Plovdiv") {
            cost = 1.30;
        } else if (city == "Varna") {
            cost = 1.35;
        }
    } else if (product == "peanuts") {
        if (city == "Sofia") {
            cost = 1.60;
        } else if (city == "Plovdiv") {
            cost = 1.50;
        } else if (city == "Varna") {
            cost = 1.55;
        }    
    }
    
    cout << cost * quantity << endl;

    return 0;
}
