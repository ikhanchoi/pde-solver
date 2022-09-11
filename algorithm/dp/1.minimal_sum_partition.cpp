#include <iostream>
using namespace std;

int minDifference(int arr[], int n){
	int sum = 0;
	for(int i = 0; i < n; i++)
		sum += arr[i];
	
	bool t[n+1][sum+1];
	for(int i=0; i<n+1; i++)
		t[i][0] = true;
	for(int j=1; j<sum+1; j++)
		t[0][j] = false;
	for(int i=1; i<n+1; i++)
		for(int j=1; j<sum+1; j++){
			if(arr[i-1]<=j)
				t[i][j] = t[i-1][j] || t[i-1][j-arr[i-1]];
			else
				t[i][j] = t[i-1][j];			
		}
	
	int ret = INT_MAX;
	for(int i=0; i<=sum/2; i++)
		if(t[n][i])
			ret = min(ret, sum-(2*i));
	return ret;
}

int main(){
	int arr[] = {1,6,11,5};
	cout << minDifference(arr,4) << endl;
}