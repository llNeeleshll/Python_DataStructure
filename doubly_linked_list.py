class Node:

    def __init__(self, data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        pass

    def insert_at_begining(self, data):

        if self.head is None:
            self.head = Node(data, None)
            return
        
        new_node = Node(data, self.head, None)
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):

        iter = self.head

        while iter:

            if iter.next is None:
                # reached end
                iter.next = Node(data, None, iter)
                break

            iter = iter.next

    def insert_at_index(self, data, index):

        if index == 0:
            self.insert_at_begining(data)

        iter = self.head
        count = 0      

        while iter:

            if count == index -1:
                next_node_add = iter.next
                iter.next = Node(data, next_node_add, iter)
                break
           
            iter = iter.next
            count += 1

    def remove_at_index(self, index):

        if index == 0:
            self.head = self.head.next

        iter = self.head
        count = 0      

        while iter:

            if count == index -1:                
                iter.next = iter.next.next
                iter.next.prev = iter
                break
           
            iter = iter.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):

        iter = self.head
        count = 0      

        while iter:

            if iter.data == data_after:
                next_node_add = iter.next
                iter.next = Node(data_to_insert, next_node_add, iter)
                break
           
            iter = iter.next
            count += 1
        pass

    def remove_at_value(self, data):

        if self.head.data == data:
            self.head = self.head.next

        iter = self.head
        count = 0      

        while iter:

            if iter.data == data:                
                iter.prev.next = iter.next
                iter.next.prev = iter.prev
                break
           
            iter = iter.next
            count += 1

    

    def print(self):
        
        print_info = ""
        iter = self.head

        while iter:
            print_info += str(iter.data) + '-->'
            iter = iter.next

        print(print_info)

ll = DoublyLinkedList()
ll.insert_at_begining(5)
ll.insert_at_begining(10)
ll.insert_at_end(589)
ll.insert_at_end(895)
ll.print()
ll.insert_at_index(69,2)
ll.print()
ll.remove_at_index(3)
ll.print()
ll.insert_after_value(69,79)
ll.print()
ll.remove_at_value(69)
ll.print()