#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;

int main() {
    int timeFirst, timeSecond, timeThird;
    cin >> timeFirst >> timeSecond >> timeThird;

    int totalTime = timeFirst + timeSecond + timeThird;
    int seconds = totalTime % 60;
    int minutes = floor(totalTime / 60);

    cout << minutes << ":" << setfill('0') << setw(2) << seconds << endl;

    return 0;
}
