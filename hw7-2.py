class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Вставка нового вузла
def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# Знаходження найменшого значення
def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.val

# Створення дерева та тестування
root = TreeNode(250)
root = insert(root, 140)
root = insert(root, 220)
root = insert(root, 444)
root = insert(root, 555)
root = insert(root, 660)
root = insert(root, 800)

print("Найменше значення у дереві:", find_min(root))
