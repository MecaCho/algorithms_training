class Node(object):
    def __init__(self):
        self.visited = set()
        self.children = None

    # recursion
    def dfs(self, node):
        self.visited.add(node)

        for next_node in node.children:
            if not next_node in self.visited:
                self.dfs(next_node)

    def generate_related_node(self, node):
        pass
        return node

    def dsf_not_recursion(self, tree):
        if tree.root is None:
            return []

        visited, stack = [], [tree.root]

        while stack:
            node = stack.pop()
            visited.append(node)

            pass

            nodes = self.generate_related_node(node)

            stack.push(nodes)



