#include <iostream>
#include <math.h>
using std::cout;
using std::cin;
using std::endl;


int main() {
    int pages;
    cin >> pages;

    int pagesPerHour;
    cin >> pagesPerHour;
    
    int readDays;
    cin >> readDays;

    double daysNeeded = round(pages / pagesPerHour / readDays);
    cout << daysNeeded << endl;

    return 0;
}
