from collections import deque
import sys
import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
# rel_path = 'running_on_fumes_chapter_2_input_sample.txt'
rel_path = 'running_on_fumes_chapter_2_input.txt'
abs_file_path = os.path.join(script_dir, rel_path)
in_file = open(abs_file_path, 'r')

out_file_check = True
rel_path = rel_path.replace('_input', '_output')
abs_file_path = os.path.join(script_dir, rel_path)
out_file = open(abs_file_path, 'w')

def printf(s, linebreak = True):
    #print(s) 
    if out_file_check:
        if linebreak:
            out_file.write(s + '\n')
        else:
            out_file.write(s)

class SegmentTree(object):  # 0-based index
    def __init__(self, N,
                 build_fn=lambda x, y: [y]*(2*x),
                 query_fn=lambda x, y: y if x is None else min(x, y),
                 update_fn=lambda x, y: y if x is None else min(x, y),
                 default_val=float("inf")):
        self.N = N
        self.H = (N-1).bit_length()
        self.query_fn = query_fn
        self.update_fn = update_fn
        self.default_val = default_val
        self.tree = build_fn(N, default_val)
        self.lazy = [None]*N

    def __apply(self, x, val):
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.N:
            self.lazy[x] = self.update_fn(self.lazy[x], val)

    def update(self, L, R, h):  # Time: O(logN), Space: O(N)
        def pull(x):
            while x > 1:
                x //= 2
                self.tree[x] = self.query_fn(self.tree[x*2], self.tree[x*2+1])
                if self.lazy[x] is not None:
                    self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])

        L += self.N
        R += self.N
        L0, R0 = L, R
        while L <= R:
            if L & 1:  # is right child
                self.__apply(L, h)
                L += 1
            if R & 1 == 0:  # is left child
                self.__apply(R, h)
                R -= 1
            L //= 2
            R //= 2
        pull(L0)
        pull(R0)

    def query(self, L, R):  # Time: O(logN), Space: O(N)
        def push(x):
            n = 2**self.H
            while n != 1:
                y = x // n
                if self.lazy[y] is not None:
                    self.__apply(y*2, self.lazy[y])
                    self.__apply(y*2 + 1, self.lazy[y])
                    self.lazy[y] = None
                n //= 2

        result = None
        if L > R:
            return result

        L += self.N
        R += self.N
        push(L)
        push(R)
        while L <= R:
            if L & 1:  # is right child
                result = self.query_fn(result, self.tree[L])
                L += 1
            if R & 1 == 0:  # is left child
                result = self.query_fn(result, self.tree[R])
                R -= 1
            L //= 2
            R //= 2
        return result

def dfs(adj, root):
    parents = [-2]*len(adj)
    parents[root] = -1
    stk = [root]
    while stk:
        node = stk.pop()
        for child in adj[node]:
            if parents[child] >= -1:
                continue
            parents[child] = node
            stk.append(child)
    return parents

def bfs(adj, C, parents, root, exclude, max_d):
    min_C = []
    q = [root]
    while q and len(min_C) <= max_d:
        new_q = []
        min_C.append(INF)
        for node in q:
            if C[node]:
                 min_C[-1] =  min(min_C[-1], C[node])
            for child in adj[node]:
                if parents[child] == node and child != exclude:
                    new_q.append(child)
        q = new_q
    return min_C

def running_on_fumes_chapter_2():
    N, M, A, B = map(int, in_file.readline().strip().split())
    A -= 1
    B -= 1
    C = [0]*N
    adj = [[] for _ in range(N)]
    for i in range(N):
        parent, C[i] =  map(int, in_file.readline().strip().split())
        parent -= 1
        if parent == -1:
            continue
        adj[i].append(parent)
        adj[parent].append(i)
    parents = dfs(adj, B)
    curr, K = A, 0
    while curr != B:
        curr = parents[curr]
        K += 1
    segment_tree = SegmentTree(K, default_val=INF)
    segment_tree.update(0, 0, 0)
    curr, prev = parents[A], A
    for i in range(1, K):
        min_C = bfs(adj, C, parents, curr, prev, min(i, M-1))
        for d, min_c in enumerate(min_C):
            if min_c == INF:
                continue
            min_cs = segment_tree.query(max(i-(M-d), 0), i-1)
            if min_cs < INF-min_c:
                segment_tree.update(i-d, i-d, min_cs+min_c)
        curr, prev = parents[curr], curr
    result = segment_tree.query(max(K-M, 0), K-1)
    return result if result != INF else -1

MAX_N = 10**6
MAX_C = 10**9
INF = (MAX_N-2)*MAX_C+1

t = int(in_file.readline())
for case in range(t):
    check_result = running_on_fumes_chapter_2()
    if(case < t - 1):
          printf('Case #{}: {}'.format(case+1, check_result))
    else:
          printf('Case #{}: {}'.format(case+1, check_result), linebreak=False)
out_file.close()

