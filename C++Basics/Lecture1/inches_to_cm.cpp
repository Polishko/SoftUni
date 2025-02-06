#include <iostream>
using std::cout;
using std::endl;
using std::string;
using std::cin;

int main() {
	const double COEFF = 2.54;
	double num;

	cin >> num;
	cout << COEFF * num << endl;

	return 0;
}

