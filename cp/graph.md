


### 구현

### 깊이 우선 탐색

그래프 연결성분 크기 구하기
```c++
bool graph[][];
int stage(int node, bool visited[V]) {
    visited[node] = true;

    int size = 1;
    for(int v=0;v<V;v++)
        if(!visited[v]&&graph[node][v])
            size += stage(v, visited);
    return size;
}
```

```c++
bool graph[][];
bool visited[V];
int stage(int node) {
    visited[node] = true;

    int size = 1;
    for(int v=0;v<V;v++)
        if(!visited[v]&&graph[node][v])
            size += stage(v);
    return size;
}
```

```c++
bool tree[][];
// tree일 때만, visited 필요 없음
int back(int node, int parent=-1) {
    int size = 1;
    for(int v=1;v<=V;v++)
        if(v!=parent&&tree[node][v])
            size += back(v, node);
    return size;
}
```

### 너비 우선 탐색

연결성분 개수 by BFS
```c++
int solution(int N, bool graph[][]) {
	int node;
	bool visited[N] = {false,};

	queue<int> que;
	int answer = 0;
	for(int root=0;root<N;root++)
		if(!visited[root]){
			answer++;
			que.push(root); // init call

			while(!que.empty()) { // stage
				// update node, visited
				node = que.front(), que.pop();
				visited[node] = true;

				for(int v=0;v<N;v++)
					if(!visited[v] && graph[node][v])
						que.push(v); // call..?
			}
		}
	return answer;
}
```
- visit과 push가, front와 pop이 함께 다닌다

플러드필
```c++
int solution(vector<vector<int>> maps)
{
	int answer = -1;
	int len[100][100];
	int x,y;
	n=maps.size(); m=maps[0].size();

	queue<pair<int,int>> que;
	que.push({0,0}); maps[0][0]=0; len[0][0]=1;
	while(!que.empty()){
		pair<int,int> node = que.front(), que.pop();
		x = node.first, y = node.second;
		maps[x][y]=0;
		if(node.first==n-1&&node.second==m-1){
			answer = len[n-1][m-1];
			break;
		}
		for(int d=0;d<4;d++){
			x1=x+dx[d], y1=y+dy[d];
			if(0<=x1&&x1<n&&0<=y1&&y1<m&&maps[x1][y1]){
				que.push({x1,y1});
				len[x1][y1]=len[x][y]+1;
			}
		}
	}
	return answer;
}
```


### 최소 스패닝 트리 (MST)
크루스칼
```c++
class Edge {
public:
	int v1, v2, w;
	bool operator < (Edge& e) {return w<e.w;}
};

class UnionFind {
public:
	vector<int> parent;
	UnionFind(int V){
		parent.resize(V);
		for(int v=0;v<V;v++)
			parent[v]=v;
	}
	void unite(int x, int y){
		x = find(x), y = find(y); // find 호출 횟수 줄이기 위함
		if(x!=y) parent[x] = y;
	}
	int find(int x){
		if(parent[x]==x) return x;
		return parent[x] = find(parent[x]) // find 재호출 시 속도 줄이기 위함
	}
}

int main()
{
	int V, E;
	cin >> V >> E;
	vector<Edge> edges;
	edges.reserve(E);
	UnionFind uf(V);

	for (int i=0;i<E;i++)
		cin >> edges[i].v1 >> edges[i].v2 >> edges[i].w;
	sort(edges,edges+E);

	int min_cost = 0, num_edge = 0;
	for (int i=0;i<E;i++) {
		if (uf.find(edges[i].v1) != uf.find(edges[i].v2))
			num_edge++,
			min_cost += edges[i].w,
			uf.unite(edges[i].v1, edges[i].v2);
		if(num_edge == V-1) break;
	}
	cout << min_cost;
	return 0;
}
```
코스트를 탐욕선택 기준으로 포레스트에 하나씩 추가하며 사이클 생기는지 확인



프림
```c++
```



### 최단 경로 (SPP)

다익스트라: 음의 가중치 불가


다익스트라
```c++
pair<int*,int*> dijkstra(int graph[][], int src){
	int dist[V]; // dist[i] = dist(src,i)
	int parent[V] = {false,};
	bool visited[V] = {false,};
	int node

	int prev, min;

	for(int i=0;i<V;i++)
		dist[i] = INT_MAX;
	dist[src] = 0;

	for(int i=0;i<V-1;i++){ // stage
		// O(VlogV) if we use heap
		// update node, parent, visited
		prev = node;
		min = INT_MAX;
		for(int v=0;v<V;v++)
			if(!visited[v]&&dist[v]<min)
				min = dist[v], node = v;
		parent[node] = prev;
		visited[node] = true;

		// O(ElogV) if we use heap
		// update dist
		for(int v=0;v<V; v++)
			if(!visited[v] && graph[node][v]
				&& dist[node] != INT_MAX
				&& dist[node] + graph[node][v] < dist[v])
				dist[v] = dist[node] + graph[node][v];
	}
	return {dist,parent};
}

```

벨만-포드

플로이드-와샬


