#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Decimal: ";
    cin >> n;
    cout << "Binary: ";
    for (int i = 31; i >= 0; --i)
        cout << ((n >> i) & 1);
    cout << endl;
    return 0;
}
