#include <iostream>
using namespace std;

int main() {
    int num;
    cin >> num;

    if (num != 0 && (num < 100 || num > 200)) {
        cout << "invalid" << endl;
    }

    return 0;
}
