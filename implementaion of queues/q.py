class Queuee:
    def __init__(self):
        self.queuee = []

    def enque(self, element):
        self.queuee.append(element)

    def deque(self):
        if not self.queuee:
            print("queue is already empty")
        else:
            print(f"qequeued element: {self.queuee.pop(0)}")

    def display(self):
        if not self.queuee:
            print("Queue is empty")
        else:
            print("Queue elements are:")
            for element in self.queuee:
                print(element)

q = Queuee()
q.enque(10)
q.enque(20)
q.display()
q.deque()
q.display()
