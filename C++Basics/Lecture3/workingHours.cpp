#include <iostream>
using namespace std;

int main() {
    int hour;
    string day;
    cin >> hour >> day;

    cout << (hour < 10 || hour > 18 || day == "Sunday" ? "closed" : "open") << endl;

    return 0;
}
