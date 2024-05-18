import networkx as nx
import matplotlib.pyplot as plt
from task1 import G, pos

# Функція пошуку шляху за допомогою DFS
def dfs_path(graph, start, end):
    visited = set()
    stack = [(start, [])]

    while stack:
        (node, path) = stack.pop()
        if node in visited:
            continue

        visited.add(node)
        path.append(node)

        if node == end:
            return path

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                stack.append((neighbor, path[:]))

# Функція пошуку шляху за допомогою BFS
def bfs_path(graph, start, end):
    visited = set()
    queue = [(start, [])]

    while queue:
        (node, path) = queue.pop(0)
        if node in visited:
            continue

        visited.add(node)
        path.append(node)

        if node == end:
            return path

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                queue.append((neighbor, path[:]))

# Функція візуалізації графу з підсвіченим шляхом
def visualize_path(graph, path, title, pos):
    plt.figure(figsize=(10, 6))
    
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, font_color='black', edge_color='gray')
    
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='r', width=2)
        nx.draw_networkx_nodes(graph, pos, nodelist=path, node_color='r', node_size=1500)
    
    plt.title(title)
    plt.show()

# Приклад знаходження шляху (від "Alina" до "Hryhoriy")
dfs_path_result = dfs_path(G, "Alina", "Hryhoriy")
bfs_path_result = bfs_path(G, "Alina", "Hryhoriy")

print()
print(f"Шлях DFS: {dfs_path_result}")
print(f"Шлях BFS: {bfs_path_result}")

# Візуалізація шляхів
visualize_path(G, dfs_path_result, "DFS шлях від Alina до Hryhoriy", pos)
visualize_path(G, bfs_path_result, "BFS шлях від Alina до Hryhoriy", pos)
print()

# Порівняння та пояснення див. у README.md