🔍 Shortest Path Visualizer (BFS)

This is a Python project. It implements a Breadth-First Search (BFS) algorithm to efficiently find the shortest path between two nodes similar to a network topology. This program uses Matplotlib's [Networkx](https://networkx.org/documentation/stable/auto_examples/basic/index.html) package.

<img src="images/BFS.png" width="400"/>

🚀 Features
- Thank you [GeeksforGeeks](https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/0) for the BFS logic. 
- Great for learning graph traversal and pathfinding basics
  
🧠 How It Works
- The program models the problem as a graph or grid
- BFS explores all neighboring nodes level by level
- The first time the destination is reached guarantees the shortest path (Prim's algorithm).
- The final path is displayed visually

  
🛠️ Tech Used

[Python](https://www.python.org/),
[Matplotlib](https://matplotlib.org/),
[Networkx](https://networkx.org/documentation/stable/auto_examples/basic/index.html)

▶️ How to Run
Make sure you have Python installed

Install dependencies:
```bash
pip install matplotlib networkx
```

Run the program:
```bash
python main.py
```
📌 Example Use Cases and Adjacency List for nodes.
Maze solving
Grid-based pathfinding
Learning graph algorithms
Visualizing traversal techniques

Example graph:
```
graph = {'A': ['B', 'E', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F', 'G'],
            'D': ['B', 'E'],
            'E': ['A', 'B', 'D'],
            'F': ['C'],
            'G': ['C']}

A connects to B, E, and C. 
```

⚠️ Notes
Works best for unweighted graphs (since BFS assumes equal edge cost)
For weighted graphs, consider algorithms like Dijkstra’s

💡 Why I Made This
I built this project to better understand graph algorithms, to learn digital visualization tools, and how shortest path problems work.
