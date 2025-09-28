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

    def search(self, value):
        curr = self.head
        while curr:
            if curr.data == value:
                return True
            curr = curr.next
        return False



N = 100000
search_value = -1   # non-existent

# Python list
py_list = list(range(N))

start = time.time()
found_list = search_value in py_list  
end = time.time()
print("Python list search: found =", found_list, "| time =", end - start)


# Linked list
ll = LinkedList()
for i in range(N):
    ll.insert_at_end(i)

start = time.time()
found_ll = ll.search(search_value)   # full traversal
end = time.time()
print("Linked list search: found =", found_ll, "| time =", end - start)
