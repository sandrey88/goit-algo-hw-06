import networkx as nx
import matplotlib.pyplot as plt
from task1 import G, pos

# Додавання ваг до ребер
edge_weights = {
    ("Alina", "Bohdan"): 2,
    ("Alina", "Maksym"): 3,
    ("Bohdan", "Maksym"): 1,
    ("Dmytro", "Olena"): 4,
    ("Olena", "Fedir"): 6,
    ("Fedir", "Hryhoriy"): 2,
    ("Hryhoriy", "Hanna"): 3,
    ("Hanna", "Inesa"): 1,
    ("Inesa", "Yaroslav"): 5,
    ("Dmytro", "Yaroslav"): 8,
    # Додаткові зв'язки
    ("Alina", "Dmytro"): 7,
    ("Bohdan", "Olena"): 3,
    ("Maksym", "Fedir"): 2,
    ("Yaroslav", "Alina"): 4,
    ("Inesa", "Maksym"): 1,
}

# Встановлення ваг для ребер
nx.set_edge_attributes(G, edge_weights, 'weight')

# Візуалізація графу
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, font_color='black', edge_color='gray')

# Додавання міток з вагами ребер
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()

# Функція для знаходження найкоротших шляхів між усіма парами вершин за допомогою алгоритму Дейкстри
def all_pairs_dijkstra(graph):
    shortest_paths = dict(nx.all_pairs_dijkstra_path(graph, weight='weight'))
    shortest_path_lengths = dict(nx.all_pairs_dijkstra_path_length(graph, weight='weight'))
    return shortest_paths, shortest_path_lengths

# Знаходження найкоротших шляхів між усіма парами вершин
all_shortest_paths, all_shortest_path_lengths = all_pairs_dijkstra(G)

# Виведення найкоротших шляхів між усіма парами вершин
print("\nНайкоротші шляхи між усіма парами вершин:")
for start_node, paths in all_shortest_paths.items():
    for end_node, path in paths.items():
        if start_node != end_node:
            path_length = all_shortest_path_lengths[start_node][end_node]
            print(f"{start_node} -> {end_node}: Шлях: {path}, Довжина: {path_length}")

print()

# Приклад знаходження найкоротшого шляху
start = "Alina"
end = "Hryhoriy"
shortest_path = all_shortest_paths[start][end]
shortest_path_length = all_shortest_path_lengths[start][end]
print(f"Найкоротший шлях від {start} до {end}: {shortest_path}")
print(f"Довжина найкоротшого шляху від {start} до {end}: {shortest_path_length}")
print()
