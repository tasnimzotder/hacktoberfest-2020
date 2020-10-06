#include<bits/stdc++.h> 
using namespace  std;

int pre(char c){
	if(c == '^') 
		return 3;
	else if(c == '*' || c == '/') 
		return 2; 
	else if(c == '+' || c == '-') 
		return 1; 
	else
		return -1;
}

void infixToPostfix(string s){
	stack<char> st;
	string ns;
	int l = s.length(); 
	st.push('N');
	for (int i = 0; i < l; i++)
	{
		if((s[i]>='a' && s[i]<='z') || (s[i]>='A' && s[i]<='Z') ){
			ns+=s[i];
		}
		else if(s[i]=='(')
			st.push('(');
		else if(s[i]==')'){
			while(st.top() !='N' && st.top() != '('){
				char x=st.top();
				st.pop();
				ns+=x;
			}

			if(st.top()=='('){
				char x=st.top();
				st.pop();
			}
		}
		else{
			while(st.top() !='N' && pre(s[i])<=pre(st.top())){
				char x=st.top();
				st.pop();
				ns+=x;
			}
			st.push(s[i]);
		}
	}
	while(st.top()!='N'){
		char x=st.top();
		st.pop();
		ns+=x;
	}
	cout<<"infix To Postfix :- "<< ns <<endl;
}

int main(){
	string str="a+b*c-(d/e+f*g*h)";
	infixToPostfix(str);
	return 0;
}