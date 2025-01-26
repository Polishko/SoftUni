#include <iostream>
#include <math.h>
#include <sstream>
using namespace std;

int main() {
    string nameSerial;
    int episodeDuration;
    int breakTime;

    getline(cin, nameSerial);

    cin >> episodeDuration >> breakTime;

    double lunch = breakTime / 8.0;
    double relaxing = breakTime / 4.0;
    double totalTimeNeeded = breakTime - (lunch + relaxing);
    double timeDifference = ceil(abs(totalTimeNeeded - episodeDuration));

    string resultString;
    if (totalTimeNeeded >= episodeDuration) {
        stringstream stream;
        stream << "You have enough time to watch " << nameSerial 
        << " and left with " << timeDifference << " minutes free time.";
        resultString = stream.str();
    } else {
        stringstream stream;
        stream << "You don't have enough time to watch " << nameSerial 
        << ", you need " << timeDifference << " more minutes.";
        resultString = stream.str();
    }

    cout << resultString << endl;
    
    return 0;
}