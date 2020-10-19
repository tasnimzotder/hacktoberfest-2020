#include<bits/stdc++.h>
using namespace std;
struct TreeNode{
	TreeNode *left;
	int val;
    TreeNode *right;
    TreeNode(int x): val(x),left(NULL),right(NULL){}
};
void create(TreeNode *&T,int a[],int i,int n){
	if(i<n){
	TreeNode *t;
	cout<<" val of i is "<<i<<"\n";
	if(a[i]==-1){
		return;
	}
	if(T==NULL){
		cout<<"entered";
		t=new TreeNode(a[i]);
		T=t;
		cout<<" so T val is "<<T->val<<"\n";
	}
		create(T->left,a,2*i+1,n);
		create(T->right,a,2*i+2,n);
  }
}
void print(TreeNode *T){
	if(T==NULL)
	return;
	print(T->left);
	cout<<T->val<<" ";
	print(T->right);
}
int main(){
	TreeNode *T=NULL;
	int a[]={1,2,3,4,5,6,7,-1,-1,-1,-1,-1,-1,-1,-1};
	int n=sizeof(a)/sizeof(a[0]);
	cout<<"n is "<<n<<"\n";
	create(T,a,0,n);
	cout<<" Tree is \n";
	print(T);
	cout<<"\n";	
	return 0;
}
