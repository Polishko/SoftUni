#include <iostream>
using std::cout;
using std::cin;
using std::endl;


int main() {
    const double POULTRY_MENU = 10.35;
    const double FISH_MENU = 12.40;
    const double VEGETARIAN_MENU = 8.15;
    const double DESSERT_COST_PERCENT = 20;
    const double DELIVERY_COST = 2.50;

    int poultryOrderCount;
    int fishOrderCount;
    int vegetarianOrderCount;

    cin >> poultryOrderCount;
    cin >> fishOrderCount;
    cin >> vegetarianOrderCount;

    double totalWithoutDessert = POULTRY_MENU * poultryOrderCount + FISH_MENU * fishOrderCount + VEGETARIAN_MENU * vegetarianOrderCount;
    double dessertCost = totalWithoutDessert * DESSERT_COST_PERCENT / 100;

    double totalCost = totalWithoutDessert + dessertCost + DELIVERY_COST;

    cout << totalCost << endl;

    return 0;
}
