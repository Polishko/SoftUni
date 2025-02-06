#include <iostream>
using std::cout;
using std::cin;
using std::endl;

int main() {
	const double DOG_FOOD_PRICE = 2.5;
	const int CAT_FOOD_PRICE = 4;
	
	int dogFoodCount;
	int catFoodCount;

	cin >> dogFoodCount;
	cin >> catFoodCount;

	cout << DOG_FOOD_PRICE * dogFoodCount + CAT_FOOD_PRICE * catFoodCount << " lv." << endl;

	return 0;
}