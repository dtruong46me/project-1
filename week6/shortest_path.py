
import sys
import queue

class Graph:
    def __init__(self, n) -> None:
        self.n = n
        self.nodes = {x: [] for x in range(1, n+1)}

    # Not using Priority Queue
    def dijkstra(self, source, target):
        distance = {x: float('inf') for x in range(1, self.n+1)}
        distance[source] = 0
        unvisited = set(range(1, self.n + 1))

        while len(unvisited) != 0:
            u = min(unvisited, key=lambda v: distance[v])

            if u == target:
                break

            unvisited.remove(u)

            for v, w in self.nodes[u]:
                tmp_dist = distance[u] + w

                if tmp_dist < distance[v]:
                    distance[v] = tmp_dist

        return distance[target]


    # Using Priority Queue
    def dijkstra_pq(self, source, target):
        distance = {x: float('inf') for x in range(1, self.n+1)}
        distance[source] = 0
        priority_queue = queue.PriorityQueue()
        priority_queue.put((0, source))

        while not priority_queue.empty():
            dist_u, u = priority_queue.get()

            if u == target:
                break

            if dist_u > distance[u]:
                continue

            for v, w in self.nodes[u]:
                tmp_dist = distance[u] + w

                if tmp_dist < distance[v]:
                    distance[v] = tmp_dist
                    priority_queue.put((distance[v], v))

        return distance[target]
        

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]

    graph = Graph(n)

    for _ in range(m):
        u, v, w = [int(x) for x in sys.stdin.readline().split()]

        graph.nodes[u].append((v, w))
        # graph.nodes[v].append((u, w))
    
    s, t = [int(x) for x in sys.stdin.readline().split()]

    result = graph.dijkstra_pq(source=s, target=t)

    print(result)


if __name__ == '__main__':
    main()

'''
5 7
2 5 87
1 2 97
4 5 78
3 1 72
1 4 19
2 3 63
5 1 18
1 5
'''