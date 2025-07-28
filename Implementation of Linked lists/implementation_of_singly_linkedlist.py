class Node:
   
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
   
    def __init__(self):
        self.head = None

    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at(self, position, data):
        if position < 0 or position > self.get_length():
            print("Invalid position")
        if position == 0:
            self.add_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        count = 0
        while count<position-1 and current:
            current = current.next
            count += 1
        new_node.next = current.next
        current.next = new_node
        return    

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def remove_first(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            self.head = self.head.next
       
    def remove_at(self, position):
        if position < 0 or position >= self.get_length():
            print(" please enter a valid position")

        if position == 0:
            self.remove_first(self)    
            return

        current = self.head
        count = 0
        while count < position - 1:
            current = current.next
            count += 1
        current.next = current.next.next
    def remove_last(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            current = self.head
            
            while current.next.next:
                current = current.next
            current.next = None



    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

    def search(self, data):
        current = self.head
        flag = 0
        while current:
            if current.data == data:
                foag =1
            current = current.next
        else:
                flag = 0
        if flag == 1:
            print(f"{data} found in the list")
        else:
            print(f"{data} not found in the list")
    def rev(self):
        current = self.head
        p = current
        p.next = None
        q =current.next
        while current.next:
            q.next = p
            p = q
            q = current.next
            current = current.next
        self.head = p
    
    
def main():
    ll = LinkedList()
    # ll.add_at_end(10)
    ll.add_at_beginning(45)
    # ll.add_at_end(20)
    ll.add_at_beginning(55)
    ll.add_at_beginning(65)
    ll.insert_at(3, 15)     
    ll.display()            
    print("Length:", ll.get_length()) 

    ll.remove_first()        
    ll.display()     
    ll.rev()
if __name__ == "__main__":
    main()           




