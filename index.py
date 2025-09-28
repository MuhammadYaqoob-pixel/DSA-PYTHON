class code:
    def __init__(self, data):
        self.data=data

        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None

    def insert_at_end(self,data):
            new_node=code(data)
            if not self.head:
                self.head=new_node
                return
            curr=self.head
            while curr.next:
                curr=curr.next
                curr.next=new_node

    def insert_at_start(self,data):
            new_node=code(data)
            new_node.next=self.head
            self.head=new_node

    def delete(self,key):
                curr=self.head
                if curr and curr.data==key:
                    self.head=curr.next
                    return
                prev=None
                while curr and curr.data!=key:
                    prev=curr
                    curr=curr.next
                if curr:
                    prev.next=curr.next

def search(self,key):
    curr=self.head
    while curr:
        if curr.data==key:
            return True
        curr=curr.next
        return False
    

import time
py_list=[]
start=time.time()
for i in range(100000):
    py_list.insert(0,i)
end=time.time()
print("python list insert at start:,", end-start)

ll=linkedlist()
start=time.time()
for i in range(100000):
    ll.insert_at_start(i)
    

end=time.time()
print("linked-list insert at:", end-start) 






