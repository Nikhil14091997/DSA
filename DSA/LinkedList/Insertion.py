class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def print_linked_list(self):
        while self.head is not None:
            print(f"{self.head.data}", end= " ")
            self.head = self.head.next
        return
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        return
    
    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return
    
    def insert_after_node(self, new_data, old_data):
        new_node = Node(new_data)
        temp = self.head
        while temp.data != old_data:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        return
        

    def insert_before_node(self, new_data, old_data):
        pass

list = LinkedList()
list.insert_at_front(1)
list.insert_at_front(2)
list.print_linked_list()
list.insert_at_end(3)
list.print_linked_list()
list.insert_after_node(new_data=4, old_data=1)
list.print_linked_list()