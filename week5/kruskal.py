import sys

class Graph:
    def __init__(self, n: int) -> None:
        self.n = n
        self.edges = []
    
    def spanning_tree(self):
        edges_copy = self.edges.copy()
        edges_copy.sort(key=lambda x: x[2])

        djs = DisjointSet(self)
        mst_edges = []

        for u, v, w in edges_copy:
            if djs.find(u) != djs.find(v):
                djs.union(u, v)
                mst_edges.append((u, v, w))
        
        total_weight = sum(w for _, _, w in mst_edges)

        return total_weight
    
    
class DisjointSet:
    def __init__(self, graph: Graph) -> None:
        self.parent = [x for x in range(graph.n + 1)]
        self.rank = [0 for x in range(graph.n + 1)]
    
    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]

    graph = Graph(n)

    for _ in range(m):
        u, v, w = [int(x) for x in sys.stdin.readline().split()]
        graph.edges.append((u, v, w))

    weight = graph.spanning_tree()

    print(weight)

if __name__ == '__main__':
    main()

'''
5 8
1 2 1
1 3 4
1 5 1
2 4 2
2 5 1
3 4 3
3 5 3
4 5 2
'''