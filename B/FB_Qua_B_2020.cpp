#include <iostream>
#include <bitset>
#include <bits/stdc++.h>
#include <limits>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <stack>
#define fo(a,X) for(int a=0;a<X;a++)

using namespace std;

char solve(int n);

int main()
{
	int t,n;
	cin>>t;
	char ans[t];
	fo(i,t)
	{
		cin>>n;
		ans[i]=solve(n);
	}
	cout<<endl;
	fo(i,t)
	cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
	return 0;
}

char solve(int n)
{
	int a=0;
	int b=0;
	char c[n];
	fo(i,n)
	{
		cin>>c[i];
		if(c[i]=='A')
		a++;
		else
		b++;
	}
	if (abs(a-b)==1)
	return 'Y';
	else
	return 'N';
}
