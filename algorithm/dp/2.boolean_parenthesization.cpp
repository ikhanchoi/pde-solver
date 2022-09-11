#include <iostream>
using namespace std;

class Solution{
public:
	unordered_map<string, int> map;
	mp.clear();

	int solve(string S, int i, int j, bool isTrue){
		if(i>j)	return 0;
		if(i==j){
			if(isTrue)
				return S[i]=='T';
			else
				return S[i]=='F';
		}

		string temp=to_string(i)+" "+to_string(j)+" "+to_string(isTrue);
		if(map.find(temp) != map.end())
			return map[temp];

		int ans = 0;
		for(int k=i+1; k<j; k+=2){
			int lt = solve(S, i, k-1, true);
			int lf = solve(S, i, k-1, false);
			int rt = solve(S, k+1, j, true);
			int rf = solve(S, k+1, j, false);
			if(S[k]=='|'){
				if(isTrue)
					ans += lt*rt + lt*rf + lf*rt;
				else
					ans += lf*rf;
			}
			else if(S[k]=='^'){
				if(isTrue)
					ans += lf*rt + lt*rf;
				else
					ans += lt*rt + lf*rf;
			}
			else if(S[k]=='&'){
				if(isTrue)
					ans += lt*rt;
				else
					ans += lt*rf + lf*rt + lf*rf;
			}
		}
		return map[temp] = ans % 1003;
	}

	int countWays(int N, string S){
		return solve(S, 0, N-1, true) % 1003;
	}
}

int main(){
	int N = 7;
	string S = "T|T&F^T";
	cout << Solution::countWays(N, S) << endl;
}