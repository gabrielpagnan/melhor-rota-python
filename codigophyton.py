import networkx as nx
import matplotlib.pyplot as plt

# Criar um grafo vazio
G = nx.Graph()

# Adicionar nós (cidades)
cidades = ["Morro da Fumaça", "Criciúma", "Içara", "Cocal do Sul", "Urussanga", "Treze de Maio", "Sangão", "Siderópolis", "Jaguaruna"]
for cidade in cidades:
    G.add_node(cidade)

# Adicionar arestas (distâncias entre cidades)
arestas = [
    ("Morro da Fumaça", "Criciúma", 17.6),
    ("Morro da Fumaça", "Sangão", 9.4),
    ("Criciúma", "Içara", 11.5),
    ("Içara", "Cocal do Sul", 14.4),
    ("Cocal do Sul", "Urussanga", 9.6),
    ("Urussanga", "Jaguaruna", 41.8),
    ("Jaguaruna", "Siderópolis", 64.2),
    ("Siderópolis", "Sangão", 42.2),
    ("Sangão", "Treze de Maio", 13.2),
    ("Treze de Maio", "Içara", 29.7),
    ("Treze de Maio", "Cocal do Sul", 39.4),
    ("Treze de Maio", "Urussanga", 38.5),
    ("Treze de Maio", "Siderópolis", 35.2)
]

for aresta in arestas:
    G.add_edge(aresta[0], aresta[1], weight=aresta[2])

# Desenhar o grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Mostrar o grafo
plt.show()