#include <iostream>
#include <math.h>
#include <sstream>
#include <iomanip>
using namespace std;

int main() {
    double previousRecord, distance, secondsPerMeter;
    cin >> previousRecord >> distance >> secondsPerMeter;

    double totalTime = distance * secondsPerMeter + floor(distance / 15) * 12.5;

    string resultString;
    if (totalTime < previousRecord) {
        ostringstream stream;
        stream << "Yes, he succeeded! The new world record is " << fixed << setprecision(2) << totalTime << " seconds.";
        resultString = stream.str();
    } else {
        ostringstream stream;
        stream << "No, he failed! He was " << fixed << setprecision(2) << totalTime - previousRecord << " seconds slower.";
        resultString = stream.str();
    }

    cout << resultString << endl; 

    return 0;
}
