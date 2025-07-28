class BubbleSort:
    def __init__(self, n):
        self.n = n
        self.data = []

    def input_numbers(self):
        print(f"Enter {self.n} numbers to be sorted:")
        for i in range(self.n):
            x = int(input(f"Enter number {i+1}: "))
            self.data.append(x)

    def sort(self):
        for i in range(self.n - 1):
            for j in range(self.n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]

    def display(self):
        print("Sorted list:", self.data)



a = BubbleSort(7)
a.input_numbers()
a.sort()
a.display()
