#include <iostream>
using namespace std;

int main() {
	int duration = 3;
	string name;
	cin >> name;
	int projectCount;
	cin >> projectCount;

	cout << "The architect " << name << " will need " << 3 * projectCount << " hours to complete " << projectCount << " project/s." << endl;
	
	return 0;
}
