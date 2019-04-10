
# min heap
# insert one item
# delete remove parent restructure tree
# get min returns top value


class Node:
    def __init__(self, value):
        self.value = value

    def set_left(self, node):
        self.left = left

    def set_right(self, node):
        self.right = right

class Heap:
    def __init__(self, node):
        self.HEAD = node

    def insert(self, value):
        print(value)
        if self.HEAD.value < value:
            new_node = Node(value)
            new_node.set_left = self.HEAD

    def delete(self):
        pass

    def get_min(self):
        return self.HEAD.value


test = [ 4, 10, 1, 6, 7,]

first = Node(3)

heap = Heap(first)

for x in test:
    heap.insert(x)

print(heap.get_min())
