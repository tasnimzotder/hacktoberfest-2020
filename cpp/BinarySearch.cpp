// C++ program to search elemnent in an array using recursive Binary Search method
#include <bits/stdc++.h>

using namespace std;

int binarySearch(int arr[], int l, int r, int x)
{
    if (r >= l) {
        int mid = l + (r - l) / 2;

        // If the element is present at the middle
        if (arr[mid] == x)
            return mid;

        // If element is smaller than mid, then it can only be present in left subarray
        if (arr[mid] > x)
            return binarySearch(arr, l, mid - 1, x);

        // Else the element can only be present in right subarray
        return binarySearch(arr, mid + 1, r, x);
    }

    // We reach here when element is not present in array
    return -1;
}

int main(void)
{
    //Array of elements
    int arr[] = { 2, 3, 4, 10, 40 };
    int x = 10; //Element to be sarched
    int n = sizeof(arr) / sizeof(arr[0]);  //Length of Array
    int result = binarySearch(arr, 0, n - 1, x);

    if(result == -1)
        cout << "Element is not present in array";
    else
        cout << "Element is present at index " << result;
    return 0;
}
