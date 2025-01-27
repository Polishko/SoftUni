#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    string fruit, day;
    double quantity;
    cin >> fruit >> day >> quantity;

    double price = 0;
    if (fruit == "banana") {
        if (day == "Saturday" || day == "Sunday") {
            price = 2.70;
        } else if (day == "Monday" || day == "Tuesday" || day == "Wednesday" || day == "Thursday" || day == "Friday") {
            price = 2.50;
        }
    } else if (fruit == "apple") {
        if (day == "Saturday" || day == "Sunday") {
            price = 1.25;
        } else if (day == "Monday" || day == "Tuesday" || day == "Wednesday" || day == "Thursday" || day == "Friday") {
            price = 1.20;
        }
    } else if (fruit == "orange") {
        if (day == "Saturday" || day == "Sunday") {
            price = 0.90;
        } else if (day == "Monday" || day == "Tuesday" || day == "Wednesday" || day == "Thursday" || day == "Friday") {
            price = 0.85;
        }
    } else if (fruit == "grapefruit") {
        if (day == "Saturday" || day == "Sunday") {
            price = 1.60;
        } else if (day == "Monday" || day == "Tuesday" || day == "Wednesday" || day == "Thursday" || day == "Friday") {
            price = 1.45;
        }
    } else if (fruit == "kiwi") {
        if (day == "Saturday" || day == "Sunday") {
            price = 3.00;
        } else if (day == "Monday" || day == "Tuesday" || day == "Wednesday" || day == "Thursday" || day == "Friday") {
            price = 2.70;
        }
    } else if (fruit == "pineapple") {
        if (day == "Saturday" || day == "Sunday") {
            price = 5.60;
        } else if (day == "Monday" || day == "Tuesday" || day == "Wednesday" || day == "Thursday" || day == "Friday") {
            price = 5.50;
        }
    } else if (fruit == "grapes") {
        if (day == "Saturday" || day == "Sunday") {
            price = 4.20;
        } else if (day == "Monday" || day == "Tuesday" || day == "Wednesday" || day == "Thursday" || day == "Friday") {
            price = 3.85;
        }
    }

    double totalPrice = price * quantity;

    price > 0 ? cout << fixed << setprecision(2) << totalPrice: cout << "error";
    cout << endl;

    return 0;
}
