class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [None] * max_size  
        self.tos = -1  
    def is_full(self):
        return self.tos == self.max_size - 1

    def is_empty(self):
        return self.tos == -1
    
    def check(self):
        print("Is stack full?", self.is_full())
        print("Is stack empty?", self.is_empty())


    def push(self, item):
        if self.is_full():
            print("Stack is full! Cannot push.")
        else:
            self.tos += 1
            self.stack[self.tos] = item
            print(f"Pushed {item} to stack.")



    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        else:
            item = self.stack[self.tos]
            self.stack[self.tos] = None  
            self.tos -= 1
            print(f"Popped {item} from stack.")
            return item
    def display(self):
        print("Current stack:", self.stack[:self.tos + 1])
    

# max_size = int(input("Enter the maximum size of the stack: "))
# stack = Stack(max_size)

s1= Stack(2)

s1.push(10)
s1.push(20)
s1.push(30) 
s1.display()







# # stack = Stack(3)
# stack.push(10)
# stack.push(20)
# stack.push(30)
# stack.push(40)  
# # stack.pop()
# # stack.pop()
# # stack.pop()
# # stack.pop()
# stack.check() 
# stack.display()