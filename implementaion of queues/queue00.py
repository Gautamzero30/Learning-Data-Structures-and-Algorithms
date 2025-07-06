front =-1
rare = -1
queue = []



def enque(element):
    global front, rare, queue
    if front ==-1 and rare ==-1:
        queue.append(element)
        front+=1
        rare+=1
    elif front ==0 and rare ==0:
        queue.append(element)
        rare+=1
    else :
        queue.append(element)
def deque():
    global front, rare, queue
    if front ==-1 and rare ==-1:
        print("the queue is already empty")

    elif front ==0 and rare ==0:
        queue.pop()
        front =-1
        rare = -1

        
    else :
        queue.pop()
        front=front+1
def display():
    global front, rare,queue
    for i in range(front, rare+1):
       head=0
       print(f"the element is {queue[i]}")
       head+=1 
enque(10)
display()
enque(20)
display()
enque(30)
display()
deque()
deque()
display()




#  we have to usse the concept of global here
