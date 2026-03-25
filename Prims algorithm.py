import networkx as nx # Undirected graph tool
import matplotlib.pyplot as plt # Visualization tool
from collections import deque

# Breadth-first-search definition
def BFS(graph, start, goal):
    explored = []
    queue = deque([[start]])
    if start == goal: return [start]

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in explored:
            neighbours = graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    return new_path # Return the path for visualization
            explored.append(node)

    # Condition when the nodes 
    # are not connected
    print("So sorry, but a connecting"\
                "path doesn't exist :(")
    return

# Example inputs and visualization implementation
if __name__ == "__main__":
    graph_dict = { 
        'A': ['B', 'E', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B', 'E'],
        'E': ['A', 'B', 'D'],
        'F': ['C'],
        'G': ['C']
    }

    # 1. Creatiing the NetworkX graph from our dictionary graph_dict
    G = nx.Graph(graph_dict)

    # 2. Running the BFS algorithm ---> Shortest path from point D to G
    path = BFS(graph_dict, 'D', 'G')
    
    # 3. Visualization input layout
    position = nx.spring_layout(G)
    node_colors = ["#7577ff" if n not in path else "#ffff5a" for n in G.nodes()]
    
    # Identify edges that are part of the shortest path
    path_edges = list(zip(path, path[1:])) if path else []
    edge_colors = ['black' if edge not in path_edges and tuple(reversed(edge)) not in path_edges else 'orange' for edge in G.edges()]

    # 4. User Interface layout
    nx.draw(G, position, with_labels=True, node_color=node_colors, edge_color=edge_colors, width=2, node_size=800)
    plt.show()
