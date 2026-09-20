def adjacency_list_to_matrix(adj_list: dict) -> list:
    nodes = len(adj_list)
    new_matrix = []

    for node in range(nodes):
        new_matrix.append([0] * nodes)
    for key in adj_list.keys():
        for value in adj_list.get(key):
            new_matrix[key][value] = 1

    for line in new_matrix:
        print(line)
    return new_matrix


my_adjacency_list = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}
adjacency_list_to_matrix(my_adjacency_list)