#include <iostream>
using namespace std;

int main() {

    string dayInput;
    cin >> dayInput;

    string resultString;
    if (dayInput == "Saturday" || dayInput == "Sunday") {
        resultString = "Weekend";
    } else if (dayInput == "Monday" || dayInput == "Tuesday" || dayInput == "Wednesday" || dayInput == "Thursday" || dayInput == "Friday") {
        resultString = "Working day";
    } else {
        resultString = "Error";
    }

    cout << resultString << endl;
    
    return 0;
}
