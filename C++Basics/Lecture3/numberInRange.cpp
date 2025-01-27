#include <iostream>
using namespace std;

int main() {
    int num;
    cin >> num;

    cout << (num >= -100 && num <= 100 && num != 0 ? "Yes" : "No") << endl;

    return 0;
}
