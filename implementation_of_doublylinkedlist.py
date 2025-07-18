class Node():
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None
class doublylinked():

    def __init__(self):
        self.head = None
        

    
    def insertatbeg(self,data):
        newnode = Node(data)  
        newnode.next = self.head
        newnode.prev= None
        if self.head is not None:
            self.head.prev = newnode
        
        self.head = newnode 

    def insertatlast(self, data):
        if self.head is None:
            self.insertatbeg(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            newnode = Node(data)
            current.next = newnode
            newnode.prev = current
            newnode.next = None
    def display(self):
        current = self .head
        while current:
            print(f"{current.data} ->",end = " ")
            current= current.next
        print("None")    

                    
d1= doublylinked ()
d1.insertatbeg(10)
d1.display()
d1.insertatbeg(4)
d1.insertatbeg(5)
d1.insertatbeg(44)
d1.insertatbeg(464)
d1.display()
d1.insertatlast(33)
d1.display()

