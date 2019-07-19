def generate_related_node(node):
    return node

def process():
    pass


def bfs(graph, start, end):
    queue = []
    queue.append([start])
    visited.add(start)

    while queue:
        node = queue.pop()
        visited.add(node)

        process(node)

        nodes = generate_related_node(nodes)

        queue.push(nodes)
