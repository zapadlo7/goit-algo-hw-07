import matplotlib.pyplot as plt
import networkx as nx

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def sum_values(self):
        return self._sum_values(self.root)

    def _sum_values(self, node):
        if node is None:
            return 0
        return node.val + self._sum_values(node.left) + self._sum_values(node.right)

    def draw_tree(self):
        if self.root is None:
            return

        graph = nx.DiGraph()
        self._add_edges(graph, self.root)
        pos = self._hierarchy_pos(graph, self.root.val)
        
        plt.figure(figsize=(12, 8))
        nx.draw(graph, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=15, font_weight='bold')
        plt.show()

    def _add_edges(self, graph, node):
        if node.left is not None:
            graph.add_edge(node.val, node.left.val)
            self._add_edges(graph, node.left)
        if node.right is not None:
            graph.add_edge(node.val, node.right.val)
            self._add_edges(graph, node.right)

    def _hierarchy_pos(self, G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
        pos = {root: (xcenter, vert_loc)}
        neighbors = list(G.neighbors(root))
        if len(neighbors) != 0:
            dx = width / 2
            nextx = xcenter - width / 2 - dx / 2
            for neighbor in neighbors:
                nextx += dx
                pos.update(self._hierarchy_pos(G, neighbor, width=dx, vert_gap=vert_gap, vert_loc=vert_loc-vert_gap, xcenter=nextx))
        return pos

# Створення дерева та тестування
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Сума всіх значень у дереві:", bst.sum_values())

# Візуалізація дерева
bst.draw_tree()
