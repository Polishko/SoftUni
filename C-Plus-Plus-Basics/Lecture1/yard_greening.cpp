#include <iostream>
using namespace std;

int main() {
	double pricePerSqm = 7.61;
	double discount = 0.18;
	double squareMeters;
	cin >> squareMeters;
	double totalPrice = pricePerSqm * squareMeters;
	double discountedPrice = totalPrice * discount;

	cout << "The final price is: " << totalPrice - discountedPrice << " lv." << endl;
	cout << "The discount is: " << discountedPrice << " lv." << endl;

	return 0;
}


