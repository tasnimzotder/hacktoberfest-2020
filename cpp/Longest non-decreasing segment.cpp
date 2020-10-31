#include<bits/stdc++.h>


using namespace std;
#define ll long long

int main() {
    ll n, max = 1, len = 1;
//Number of digits in array
    cout << "Number of values you want to enter: ";
    cin >> n ;
    int ar[n];
//Input values into array
    cout << "Enter the values here: ";
    for (int i = 0; i < n; i++) {
        cin >> ar[i];
    }

    for (int i = 1; i <= n - 1; i++) {
// Checks if the second sub-sequent values is greater or not
        if (ar[i] >= ar[i - 1]) {
            len++;
        }
        else {
//Modifies the value of max according to the count of matching values
            if (max <= len) {
                max = len;
            }
//Resets the count to 1 till we find the maximum value
            len = 1;
        }
    }
    if (max <= len) {
        max = len;
    }
    cout << max;
    return 0;
}
