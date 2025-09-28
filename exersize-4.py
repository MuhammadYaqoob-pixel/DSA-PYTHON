import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node


# ----------- MEMORY TEST -----------

N = 1000

# Python list
py_list = list(range(N))
list_size = sys.getsizeof(py_list)   # container size only
list_elements_size = sum(sys.getsizeof(x) for x in py_list)   # integers inside
total_list_size = list_size + list_elements_size

# Linked list
ll = LinkedList()
for i in range(N):
    ll.insert_at_end(i)

# Traverse to calculate node sizes
curr = ll.head
nodes_size = 0
while curr:
    nodes_size += sys.getsizeof(curr)
    nodes_size += sys.getsizeof(curr.data)
    curr = curr.next

ll_size = sys.getsizeof(ll) + nodes_size


# Print results
print("Python list:")
print("  Container size =", list_size)
print("  Elements size =", list_elements_size)
print("  Total size    =", total_list_size)

print("\nLinked list:")
print("  Total size    =", ll_size)
