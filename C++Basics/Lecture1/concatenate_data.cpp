#include <iostream>

using std::cout;
using std::cin;
using std::string;
using std::endl;

int main() {
	string firstName;
	string lastName;
	int age;
	string town;

	cin >> firstName;
	cin >> lastName;
	cin >> age;
	cin >> town;

	cout << "You are " << firstName << " " << lastName << ", a " << age << "-years old person from " << town << "." << endl;

	return 0;
}


