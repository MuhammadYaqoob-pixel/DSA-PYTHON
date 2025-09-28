import time


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

    def insert_at_index(self, index, data):
        """Insert at a specific index in the linked list."""
        new_node = Node(data)
        if index == 0:  # insert at start
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        count = 0
        while curr and count < index - 1:
            curr = curr.next
            count += 1

        if not curr:  # index out of range
            return

        new_node.next = curr.next
        curr.next = new_node


N = 100000
target_index = 5000
insert_value = -1

# Python list test
py_list = list(range(N))
start = time.time()
py_list.insert(target_index, insert_value)  # O(n) shift
end = time.time()
print("Python list: inserted at index", target_index, "| time =", end - start)

# Linked list test
ll = LinkedList()
for i in range(N):
    ll.insert_at_end(i)

start = time.time()
ll.insert_at_index(target_index, insert_value)  # O(n) traversal
end = time.time()
print("Linked list: inserted at index", target_index, "| time =", end - start)
