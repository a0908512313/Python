class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self.build(arr, 2 * node, start, mid)
        self.build(arr, 2 * node + 1, mid + 1, end)
        self.tree[node] = self.tree[2 * node] | self.tree[2 * node + 1]

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left = self.query(2 * node, start, mid, l, r)
        right = self.query(2 * node + 1, mid + 1, end, l, r)
        return left | right


# 讀取輸入
n = int(input())
arr = list(map(int, input().split()))
q = int(input())

# 建立線段樹
seg_tree = SegmentTree(arr)

# 處理查詢
for _ in range(q):
    l, r = map(int, input().split())
    result = seg_tree.query(1, 0, n - 1, l - 1, r - 1)
    print(result)
