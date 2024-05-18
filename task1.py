import networkx as nx
import matplotlib.pyplot as plt

# Створення порожнього графу
G = nx.Graph()

# Додавання користувачів до графу (вершини)
users = [
    "Alina",
    "Bohdan",
    "Maksym",
    "Dmytro",
    "Olena",
    "Fedir",
    "Hryhoriy",
    "Hanna",
    "Inesa",
    "Yaroslav",
]
G.add_nodes_from(users)

# Додавання дружніх зв'язків між користувачами (ребра)
edges = [
    ("Alina", "Bohdan"),
    ("Alina", "Maksym"),
    ("Bohdan", "Maksym"),
    ("Dmytro", "Olena"),
    ("Olena", "Fedir"),
    ("Fedir", "Hryhoriy"),
    ("Hryhoriy", "Hanna"),
    ("Hanna", "Inesa"),
    ("Inesa", "Yaroslav"),
    ("Dmytro", "Yaroslav"),
    # Додаткові зв'язки
    ("Alina", "Dmytro"),
    ("Bohdan", "Olena"),
    ("Maksym", "Fedir"),
    ("Yaroslav", "Alina"),
    ("Inesa", "Maksym"),
]
G.add_edges_from(edges)

# Візуалізація графу
plt.figure(figsize=(10, 6))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, font_color='black', edge_color='gray')
plt.show()

# Аналіз характеристик графу:
# Кількість вершин
num_nodes = nx.number_of_nodes(G)
print(f"Кількість вершин: {num_nodes}")

# Кількість ребер
num_edges = nx.number_of_edges(G)
print(f"Кількість ребер: {num_edges}")

# Ступінь вершин
degree_dict = dict(G.degree())
print("Ступені кожної вершини:")
for node, degree in degree_dict.items():
    print(f"{node}: {degree}")

# Розподіл ступенів вершин
degree_distribution = {}
for degree in degree_dict.values():
    if degree in degree_distribution:
        degree_distribution[degree] += 1
    else:
        degree_distribution[degree] = 1

print("Розподіл ступенів вершин:")
for degree, count in degree_distribution.items():
    print(f"{degree}: {count}")
