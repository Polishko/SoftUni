#include <iostream>
using std::cout;
using std::endl;
using std::string;
using std::cin;

int main() {
	const int DURATION = 3;
	int projectCount;
	string name;

	cin >> name;
	cin >> projectCount;

	cout
	 << "The architect " << name << " will need " << 3 * projectCount
	  << " hours to complete " << projectCount << " project/s." << endl;
	
	return 0;
}
