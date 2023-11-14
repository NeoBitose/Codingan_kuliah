class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None
        

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node= new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n= n.ref
        n.ref = new_node;
    
    def get_sum(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        total = 0
        while n is not None:
            total += n.item
            n = n.ref
        return total
    
    def get_count(self):
        if self.start_node is None:
            return 0;
        n = self.start_node
        count = 0;
        while n is not None:
            count = count + 1
            n = n.ref
        return count
    
    def traverse_list(self):
        if not self.start_node:
            print("List has no element.")
            return
        n = self.start_node
        while n:
            print(n.item, end=" -> ")
            n = n.ref
        print("Null")

    def concatenate_linked_list(self, data_list, place):
        if place.lower() == 'end':
            if self.start_node is None:
                self.start_node = data_list.start_node
            else:
                n = self.start_node
                while n.ref is not None:
                    n = n.ref
                n.ref = data_list.start_node
        elif place.lower() == 'start':
            n = data_list.start_node
            while n.ref is not None:
                n = n.ref
            n.ref = self.start_node
            self.start_node = data_list.start_node

    def insert_sorted_data(self, data):
        new_node = Node(data)
        if self.start_node is None or data <= self.start_node.item:
            new_node.ref = self.start_node
            self.start_node = new_node
        else:
            current = self.start_node
            while current.ref is not None and current.ref.item < data:
                current = current.ref
            new_node.ref = current.ref
            current.ref = new_node
    
    def reverse_linked_list(self):
        prev_node = None
        n = self.start_node
        while n is not None:
            next_node = n.ref
            n.ref = prev_node
            prev_node = n
            n = next_node
        self.start_node = prev_node

    def clear(self):
        self.start_node = None

if __name__ == "__main__":
    listinteger1 = LinkedList()
    listinteger2 = LinkedList()

    listinteger1.insert_at_start(3)
    listinteger1.insert_at_start(65)
    listinteger1.insert_at_start(1)
    listinteger1.insert_at_start(3)
    print("Linked List 1 : ")
    listinteger1.traverse_list()

    listinteger2.insert_at_end(10)
    listinteger2.insert_at_end(9)
    listinteger2.insert_at_end(12)
    listinteger2.insert_at_end(5)
    listinteger2.insert_at_end(6)
    print("\nLinked List 2 :")
    listinteger2.traverse_list()

    print("\nMencari banyak anggota dari linked list :")
    print(f"Linked List 1 : {listinteger1.get_count()}")
    print(f"Linked List 2 : {listinteger2.get_count()}")

    print("\nMenghitung jumlah seluruh nilai dari linked list :")
    totalLinkedList1 = listinteger1.get_sum()
    totalLinkedList2 = listinteger2.get_sum()

    print(f"Linked List 1 : {totalLinkedList1}")
    print(f"Linked List 2 : {totalLinkedList2}")

    print("\nConcatenate Linked List :")
    listinteger1.concatenate_linked_list(listinteger2,"start")
    listinteger1.traverse_list()

    print("\nMenambahkan data ke Linked List dalam kondisi terurut : ")
    listinteger1.clear()
    listinteger1.insert_sorted_data(3)
    listinteger1.insert_sorted_data(1)
    listinteger1.insert_sorted_data(2)
    listinteger1.insert_sorted_data(5)
    listinteger1.traverse_list()

    print("\nReverse Linked List : ")
    listinteger1.reverse_linked_list()
    listinteger1.traverse_list()