#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n;
	cin >> n;

	vector<int> arr;
	for (int i = 0; i < n; ++i) {
		int tmp;
		cin >> tmp;
		arr.push_back(tmp);
	}

	for (int i = 0; i < n; ++i) {
		int prime = 2;
		for (int j = 2; j < arr[i]; ++j) {
			if (arr[i]%j == 0) {
				++prime;
			}
			if (prime > 3) {
				cout << "NO" << endl;
			}
		}
		if (prime == 2) {
			cout << "NO" << endl;
		}else if (prime == 3){
			cout << "YES" << endl;
		}
	}

	return 0;
}
