#include<iostream>
#include<set>
#include<utility>
#include<algorithm>
using namespace std;
int main()
{
    int n, arr[100],count,k=0;
    set<pair<int,int>>vect;
    cout<<"Enter the number of elements in the array: ";
    cin>>n;
    cout<<"Enter the elements in the array: ";
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    for(int i=0;i<n;i++)
    {
        count=0;
        for(int j=0;j<n;j++)
        {
            if(arr[i]==arr[j])
            {
                count++;
            }
        }
        vect.insert(make_pair(arr[i],count));
    }
    for (auto const &p: vect) {
		cout<<"(" << p.first << "," << p.second<<")" <<" ";
	}
    cout<<endl;


    return 0;
}