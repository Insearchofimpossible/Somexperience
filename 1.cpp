#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
int main() {
    int n = pow(10,5);
    int k = 23;
    int temp = 0;
    vector<int> a;
    for (int i = 1; i <= n; i++) {
        a.push_back(i);
    }
    while (a.size() > 1) {
        temp = (temp + k - 1) % a.size();
        a.erase(a.begin() + temp);
    }

    cout << a[0] << endl;

    return 0;
}
