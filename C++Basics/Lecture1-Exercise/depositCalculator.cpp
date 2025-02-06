#include <iostream>
#include <iostream>
using std::cout;
using std::cin;
using std::endl;
using std::ios;

int main() {
    double deposit;
    cin >> deposit;

    int duration;
    cin >> duration;
    
    double percentPerYear;
    cin >> percentPerYear;

    double resultSum = deposit + duration * ((deposit * percentPerYear / 100) / 12);

    cout.setf(ios::fixed);
    cout.precision(2);
    cout << resultSum << endl;

    return 0;
}
