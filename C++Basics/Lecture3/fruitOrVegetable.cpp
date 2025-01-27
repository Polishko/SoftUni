#include <iostream>
using namespace std;

int main() {
    string product;
    cin >> product;

    string productType;
    if (product == "banana" || product == "apple" || product == "kiwi" || product == "cherry" || product == "lemon" || product == "grapes") {
        productType = "fruit";
    } else if (product == "tomato" || product == "cucumber" || product == "pepper" || product == "carrot") {
        productType = "vegetable";
    } else {
        productType = "unknown";
    }

    cout << productType << endl;

    return 0;
}
