#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string number, int k) {
    int size = number.size();
    const int last_size = size - k;
    for (int i = 0; i < size - 1; ++i) {
        if(size == last_size) {
            break;
        }
        if(number[i]  < number[i+1]) {
            number.erase(i, 1);
            i = -1;
            size -= 1;
        }
    }
    if (number.size() > last_size) {
        number.erase(last_size, number.size()-last_size);
    }
    return number;
}
