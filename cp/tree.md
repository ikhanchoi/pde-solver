
### 구현

일반적인 트리
이진트리


### 힙/우선순위 큐


```c++
vector<int> heap; // max heap
void insert(int x){ // sift up
	heap.push_back(x)
	int node = heap.size()-1;
	while(node>1){
		if(heap[node/2]<heap[node])
			swap(heap[node/2],heap[node]),
			node/=2;
		else break;
	}
}

void siftDown(int node){
	while(node*2<=heap.size()-1)
		if(node*2==heap.size()-1)
			if(heap[node]<heap[node*2])
				swap(heap[node],heap[node*2]),
				node = node*2;
			else break;
		else
			if(heap[node]<heap[node*2]||heap[node]<heap[node*2+1])
				if(heap[node*2]>heap[node*2+1])
					swap(heap[node],heap[node*2]),
					node = node*2;
				else
					swap(heap[node],heap[node*2+1]),
					node = node*2+1;
			else break;
}

void pop(){
	heap[1] = heap.back(), heap.pop_back();
	siftDown(1);
}

void heapify(vector<int>& arr){ // sift down, O(n)
	heap.clear(), heap.push_back(-1);
	for(int i=0;i<arr.size();i++)
		heap.push_back(arr[i]);
	for(int i=heap.size()-1;i>=1;i--)
		siftDown(i);
}
```




### 이진탐색트리
AVL

```c++
class Node {
public:
	int key;
	Node* left;
	Node* right;
	Node(int key) {
		this.key=key;
		left=NULL;
		right=NULL;
	}
};

void rotateLeft(Node** node){
	return;
}

int main(){
	Node* root = new Node(1);
	root->left = new Node(2);
	root->right = new Node(3);

	rotateLeft(&root);
}

```

### 게임트리



### 구간트리


```c++
class SegTree {
public:
	vector<int> seg;
	int n;

	SegTree(const vector<int>& arr){
		n = arr.size();
		init(arr);
	}
	int init(const vector<int>& arr, int a=0, int b=n-1, int node=1){
		if(a==b) return seg[node] = arr[a];
		int m=(a+b)/2;
		return seg[node] = init(arr,a,m,node*2)+init(arr,m+1,b,node*2+1);
	}
	int query(int l, int r, int a=0, int b=n-1, int node=1){
		if(b<l || r<a) return 0;
		if(l<=a && b<=r) return seg(node);
		int m=(a+b)/2;
		return query(l,r,a,m,node*2)+query(l,r,m+1,b,node*2+1);
	}
}
```




### 트라이

