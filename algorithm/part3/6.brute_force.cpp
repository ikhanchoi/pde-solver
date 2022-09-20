//----------------//
#include <sstream>
#include <iostream>
using namespace std;
#define cin in
stringstream cin;
//----------------//





#include <iostream>
using namespace std;

class PICNIC{
	int N, M;
	bool adj[10][10] = {false};

	int countPairings(bool* paired){
		int i = -1;
		for(int n = 0; n < N; n++)
			if(!paired[n]){
				i = n;
				break;
			}
		if(i == -1) return 1;

		int ret = 0;
		for(int j = i + 1; j < N; j++)
			if(!paired[j] && adj[i][j]){ // promising
				paired[i] = paired[j] = true;
				ret += countPairings(paired);
				paired[i] = paired[j] = false;
			}
		return ret;
	}

public:
	void solve(){
		cin >> N >> M;
		for(int m = 0; m < M; m++){
			int i,j;
			cin >> i >> j;
			adj[i][j] = adj[j][i] = true;
		}

		bool paired[10] = {false};
		cout << countPairings(paired) << endl;
	}
};




// 완성 안됨
#include <iostream>
using namespace std;
class BOARDCOVER{
	int H, W;
	bool board[20][20];
	int numBlock = 0;
	const int coverType[4][3][2] = {
		{ {0, 0}, {1, 0}, {0, 1} },
		{ {0, 0}, {1, 0}, {1, 1} },
		{ {0, 0}, {-1,1}, {0, 1} },
		{ {0, 0}, {0, 1}, {1, 1} }
	};
	void setBlock(){

	}
	int countCover(bool** ){
		int  = -1,  = -1;
		for(int j = 0; j < H; j++)
			for(int i = 0; i < W; i++){
				if()
			}
	}

public:
	void solve(){
		cin >> H >> W;
		char color;
		for(int j = 0; j < H; j++)
			for(int i = 0; i < W; i++){
				cin >> color;
				if(color == '.'){
					board[i][j] = true;
					numBlock++;
				else if(color == '#') board[i][j] = false;
			}

		if(numBlock % 3 != 0)
			cout << 0 << endl;
		else
			cout << countCover() << endl;
	}
};





#include <iostream>
using namespace std;
class CLOCKSYNK{
	
};





#include <iostream>
#include <vector>
using namespace std;

class FESTIVAL{
	int N, L;
	vector<int> cost;

	bool compareFrac(pair<int,int> p, pair<int,int> q){
		if(p.first * q.second > q.first * p.second) return true;
		else return false;
	}

	double minAvg(){
		vector<int> sum(N+1);
		sum[0] = 0;
		for (int i = 0; i < N; i++)
			sum[i+1] = sum[i] + cost[i];

		pair<int,int> ret(1,0), tmp;
		for(int l = L; l < 2*L && l <= N; l++){
			tmp.second = l;
			for(int a = 0; a <= N-l; a++){
				tmp.first = sum[a+l] - sum[a];
				if(compareFrac(ret, tmp))
					ret = tmp;
			}
		}
		return ret.first / (double)ret.second;
	}

public:
	void solve(){
		cin >> N >> L;
		cost.reserve(N);
		for (int n = 0; n < N; n++)
			cin >> cost[n];

		cout << minAvg() << endl;
		//printf("%.12f\n", minAvg(cost, L));
	}
};






const char* PICNIC_example_input =
	"3\n"
	"2 1\n"
	"0 1\n"
	"4 6\n"
	"0 1 1 2 2 3 3 0 0 2 1 3\n"
	"6 10\n"
	"0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5";

const char* FESTIVAL_example_input =
	"2\n"
	"6 3\n"
	"1 2 3 1 2 3\n"
	"6 2\n"
	"1 2 3 1 2 3";



int main(){
	cin << PICNIC_example_input;//
	int C;
	cin >> C;
	while(C--) PICNIC().solve();
}