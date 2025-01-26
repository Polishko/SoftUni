#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;

int main() {
    const int periodInMinutes = 15;
    int hour, minutes;
    cin >> hour >> minutes;

    int totalMinutes = periodInMinutes + minutes;
    int hoursToAdd = floor(totalMinutes / 60);
    int finalMinutes = totalMinutes % 60;

    int finalHour = (hour + hoursToAdd) % 24;

    cout << finalHour << ":" << setfill('0') << setw(2) << finalMinutes << endl;

    return 0;
}
