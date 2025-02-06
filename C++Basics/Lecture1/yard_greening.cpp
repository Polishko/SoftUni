#include <iostream>
using namespace std;

int main() {
	const double PRICE_PER_SUM = 7.61;
	const double DISCOUNT = 0.18;
	double squareMeters;
	
	cin >> squareMeters;
	double totalPrice = PRICE_PER_SUM * squareMeters;
	double discountedPrice = totalPrice * DISCOUNT;

	cout << "The final price is: " << totalPrice - discountedPrice << " lv." << endl;
	cout << "The DISCOUNT is: " << discountedPrice << " lv." << endl;

	return 0;
}


