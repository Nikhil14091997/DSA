class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def print_linked_list(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.data}", end=" ")
            temp = temp.next
        print()  # Add a newline after printing the list

    
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
    
    def insert_after_value(self, new_data, old_data):
        new_node = Node(new_data)
        temp = self.head

        while temp is not None:
            if temp.data == old_data:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next

        print(f"\n{old_data} not found in the linked list. Insertion failed.")

        

    def insert_before_node(self, new_data, old_data):
        temp = self.head
        new_node = Node(new_data)
        if temp.data == old_data:
            print("Insertion at head condition")
            new_node.next = temp
            self.head = new_node
        else:
            while temp.next.data != old_data and temp.next is not None:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        return

list = LinkedList()
list.insert_at_front(1)
list.insert_at_front(2)
list.print_linked_list()
list.insert_at_end(3)
list.print_linked_list()
list.insert_after_value(new_data=4, old_data=1)
list.print_linked_list()
list.insert_before_node(new_data=5, old_data=4)
list.print_linked_list()
list.insert_before_node(new_data=6, old_data=2)
list.print_linked_list()