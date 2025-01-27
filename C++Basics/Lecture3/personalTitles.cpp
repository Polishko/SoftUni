#include <iostream>
using namespace std;

int main() {
    double age;
    string gender;

    cin >> age >> gender;

    string resultString;
    if (gender == "f") {
        if (age < 16) {
            resultString = "Miss";
        } else {
            resultString = "Ms.";
        }
    } else if (gender == "m") {
        if (age < 16) {
            resultString = "Master";
        } else {
            resultString = "Mr.";
        }
    }

    cout << resultString << endl;

    return 0;
}