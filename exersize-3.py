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

    def get(self, index):
        curr = self.head
        count = 0
        while curr:
            if count == index:
                return curr.data
            curr = curr.next
            count += 1
        return None
    
    def delete_by_value(self, value):
        # If head is to be deleted
        if self.head and self.head.data == value:
            self.head = self.head.next
            if not self.head:   # if list becomes empty
                self.tail = None
            return True

        # Traverse for value
        prev = None
        curr = self.head
        while curr:
            if curr.data == value:
                prev.next = curr.next
                if curr == self.tail:   # if tail is deleted
                    self.tail = prev
                return True
            prev = curr
            curr = curr.next
        return False   # value not found


# ----------- TESTING -----------

N = 100000
target_index = 5000
delete_value = 12345

# Python list test
py_list = list(range(N))

# Access test
start = time.time()
val_list = py_list[target_index]
end = time.time()
print("Python list (get): value =", val_list, "| time =", end - start)

# Delete test
start = time.time()
py_list.remove(delete_value)   # O(N) worst-case
end = time.time()
print("Python list (delete by value): time =", end - start)


# Linked list test
ll = LinkedList()
for i in range(N):
    ll.insert_at_end(i)

# Access test
start = time.time()
val_ll = ll.get(target_index)
end = time.time()
print("Linked list (get): value =", val_ll, "| time =", end - start)

# Delete test
start = time.time()
ll.delete_by_value(delete_value)   # O(N)
end = time.time()
print("Linked list (delete by value): time =", end - start)
