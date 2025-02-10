from AVL_tree import insert, min_value_node, max_value_node, pre_order_traversal

root = None
keys = [10, 20, 30, 25, 28, 27, 40, 2, 15, 10, 20]

for key in keys:
    root = insert(root, key)

print("AVL-Дерево:")
print(root)

print("#first task")
print("Max value - ", max_value_node(root))

print("#second task")
print("Min value - ", min_value_node(root))

print("#third task")
path = []
pre_order_traversal(root, path)
print("Sum - ", sum(path))
