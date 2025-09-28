import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None   # keep track of last node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node   # update tail
# get function



    def get(self, index):
        curr = self.head
        count = 0
        while curr:
            if count == index:
                return curr.data
            curr = curr.next
            count += 1
        return None  


N = 100000
target_index = 5000

# Python list test
py_list = list(range(N))
start = time.time()
val_list = py_list[target_index]
end = time.time()
print("Python list: value =", val_list, "| time =", end - start)

# Linked list test
ll = LinkedList()
for i in range(N):
    ll.insert_at_end(i)

start = time.time()
val_ll = ll.get(target_index)
end = time.time()
print("Linked list: value =", val_ll, "| time =", end - start)
