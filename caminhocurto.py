#Importar as bibliotecas utilizadas para gerar grafo
import heapq
import networkx as nx
import matplotlib.pyplot as plt

#Esse código calcula a menor distância de um nó inicial para todos os outros em um grafo, rastreando os caminhos mínimos.
def dijkstra_with_path(graph, start):
    distances = {vertex: float('infinity') for vertex in graph.nodes()}
    distances[start] = 0
    previous_nodes = {vertex: None for vertex in graph.nodes()}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

# Função para obter o caminho mínimo
def get_shortest_path(previous_nodes, start, target):
    path = []
    current_node = target

    while current_node and current_node != start:
        path.append((previous_nodes[current_node], current_node))
        current_node = previous_nodes[current_node]

    path.reverse()
    return path

# Criar o grafo
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

# Executar o algoritmo de Dijkstra
start_vertex = "Morro da Fumaça"
distances, previous_nodes = dijkstra_with_path(G, start_vertex)

# Obter caminhos mínimos para todas as cidades
shortest_paths = []
for target in G.nodes():
    if target != start_vertex:
        shortest_paths.extend(get_shortest_path(previous_nodes, start_vertex, target))

# Exibir as distâncias mínimas
for city, distance in distances.items():
    print(f"Distância mínima de {start_vertex} para {city}: {distance:.2f} km")

# Desenhar o grafo
pos = nx.spring_layout(G)

# Colorir as arestas
edge_colors = []
for edge in G.edges():
    if edge in shortest_paths or (edge[1], edge[0]) in shortest_paths:
        edge_colors.append('red')
    else:
        edge_colors.append('black')

# Desenhar nós e arestas
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", edge_color=edge_colors)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Mostrar o grafo
plt.show()
