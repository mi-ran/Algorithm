#include <iostream>
#include <vector>

using namespace std;

void search(const vector<int>& arr, const int& target, int start, int end) {
	int idx = (start + end) /2;
	while(true) {
		if (arr[idx] == target) {
			cout << idx + 1 << endl;
			return;
		} else if (arr[idx] > target) {
			if (idx == 0 || arr[idx - 1] < target) {
				cout << idx + 1 << endl;
				return;
			}
			return search(arr, target, start, idx);
		} else if (arr[idx] < target) {
			return search(arr, target, idx, end);
		}
	}
}

int main() {
	int a, b;
	vector<int> aList;
	vector<int> bList;
	cin >> a;
	for (int i = 0; i < a; ++i) {
		int tmp;
		cin >> tmp;
		aList.push_back(tmp);
	}

	vector<int> arr;
	arr.push_back(aList[0]);
	for (int i = 1; i < a; ++i) {
		arr.push_back(arr[i-1] + aList[i]);
	}

	cin >> b;
	for (int i = 0; i < b; ++i) {
		int tmp;
		cin >> tmp;
		bList.push_back(tmp);
	}

	for (int i = 0; i < b; ++i) {
		search(arr, bList[i], 0, a);
	}
	return 0;
}
