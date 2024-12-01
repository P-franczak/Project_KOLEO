import math

graph = [
    [0, 5, 8, 3, 0, 0, 0, 0, 0, 4],
    [5, 0, 6, 0, 7, 0, 0, 0, 0, 0],
    [8, 6, 0, 2, 4, 9, 0, 0, 0, 0],
    [3, 0, 2, 0, 0, 1, 5, 0, 0, 0],
    [0, 7, 4, 0, 0, 3, 2, 6, 0, 0],
    [0, 0, 9, 1, 3, 0, 0, 0, 4, 0],
    [0, 0, 0, 5, 2, 0, 0, 3, 7, 0],
    [0, 0, 0, 0, 6, 0, 3, 0, 2, 5],
    [0, 0, 0, 0, 0, 4, 7, 2, 0, 8],
    [4, 0, 0, 0, 0, 0, 0, 5, 8, 0],
]  # Słownik grafu

adj_list = [
    list([i if vertice[i] else math.inf for i in range(0, len(vertice))])
    for vertice in graph
]  # Lista sąsiedzctwa każdego wierzchołka

for x in adj_list:
    while math.inf in x:
        x.remove(math.inf)


# Funkcja zwracająca wagę krawędzi pomiędzy podanymi wierzchołkami. Jeśli nie ma krawędzi zwróci inf
def weight(v1, v2):
    return graph[v1][v2] if graph[v1][v2] else math.inf


def dijkstra(graph, weight, v0, adj_list):
    vertices = [x for x in range(0, len(graph))]  # Wierzchołki grafu
    # Stworzenie tablicy wierzchołków poprzednich
    prevs = []
    # Stworzenie wag krawędzi z wierzchołkiem poprzednim
    v_weight = [math.inf for x in vertices]
    unchecked_vertices = vertices
    last_vertice = unchecked_vertices.pop(v0)
    v_weight[last_vertice] = 0
    while unchecked_vertices:
        # Dla każdego sąsiada ostatnio wybranego wierzchołka
        for vertice in adj_list[last_vertice]:
            if (
                vertice in unchecked_vertices
                and v_weight[last_vertice] + weight(last_vertice, vertice)
                < v_weight[vertice]
            ):
                # Droga do poprzedniego staje się drogą do ostatnio wybranego
                v_weight[vertice] = (
                    weight(last_vertice, vertice) + v_weight[last_vertice]
                )
                if vertice not in prevs:
                    prevs.append(vertice)
        # Szukamy wierzchołka do którego prowadzi najkrótsza droga
        min_weight = math.inf
        for vertice in unchecked_vertices:
            if v_weight[vertice] <= min_weight:
                min_weight = v_weight[vertice]
                min_vertice = vertice
        last_vertice = min_vertice  # Ustawiamy ostatnio wybrany wierzchołek na ten do którego prowadzi najkrótsza droga
        # Usuwamy z listy poprzednio wybrany wierzchołek
        unchecked_vertices.remove(last_vertice)
        # Dodajemy wagę dodanej krawędzi do wagi końcowej
    return v_weight, prevs  # Zwracamy listę krawędzi i wagę końcową


print(dijkstra(graph, weight, 0, adj_list))