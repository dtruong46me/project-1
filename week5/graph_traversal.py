import sys

class Graph:
    def __init__(self) -> None:
        self.nodes = dict()

    # Breath First Search
    def bfs(self, start_node=1) -> list:
        # Create a queue,  put into queue
        queue = [start_node]

        # Mark start node as visited
        visited = set()

        result = list()

        # While queue is not empty
        while len(queue) != 0:
            
            # Remove the head of queue and mark visited
            curr_node = queue.pop(0)
            visited.add(curr_node)

            result.append(curr_node)

            for i in self.nodes[curr_node]:
                if i not in visited and i not in queue:
                    queue.append(i)
        
        # Check all nodes are visited:
        if len(visited) != len(self.nodes.keys()):
            for u in self.nodes.keys():
                if u not in visited and len(queue) == 0:
                    queue.append(u)

                    while len(queue) != 0:
                        curr = queue.pop(0)
                        visited.add(curr)
                        result.append(curr)

                        for v in self.nodes[curr]:
                            if v not in visited and i not in queue:
                                queue.append(v)

        return result
    

    # Depth First Search
    def dfs(self, start_node=1):
        stack = [start_node]
        visited = set()
        result = [start_node]

        while len(stack) != 0:
            curr_node = stack.pop()

            for u in self.nodes[curr_node]:
                if u not in visited and u not in result:
                    visited.add(u)
                    result.append(u)

                    stack.append(curr_node)
                    stack.append(u)

                    break
        
        return result

def main():
    graph = Graph()

    n, m = [int(x) for x in sys.stdin.readline().split()]
    graph.nodes = {x: set() for x in range(1, n+1)}

    for _ in range(m):
        u, v = [int(x) for x in sys.stdin.readline().split()]

        graph.nodes[u].add(v)
        graph.nodes[v].add(u)
    
    for node in graph.nodes:
        graph.nodes[node] = list(graph.nodes[node])
        graph.nodes[node].sort()
        # print(graph.nodes.items())
    
    start_node = 1

    print(*graph.dfs(start_node))

if __name__ == '__main__':
    main()

'''
16 16
2 4
1 3
3 4
5 6
1 2
3 5
2 3
7 2
6 9
9 10
4 10
5 11
8 12
12 14
13 15
13 16
'''