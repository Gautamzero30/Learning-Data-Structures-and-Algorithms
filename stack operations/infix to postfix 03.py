# Conversion of infix expression to postfix expression using stack
class Conversion:
    def __init__(self):
        self.stack = []
        self.output = []
        self.dict = {
            "(": 0,
            ")": 0,
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "^": 3
        }

    def input(self):
        expression = input("Enter the infix expression (with spaces between tokens): ")
        self.conversion_to(expression)
        self.display()

    def conversion_to(self, expression):
        chars = expression.split()
        for char in chars:
            if char.isdigit() or char.isalpha():
                self.output.append(char)
            elif char in self.dict:
                self.checkit(char)
            else:
                print(f"Invalid operator in the expression character: {char}")
                return

       
        while self.stack:
            self.output.append(self.stack.pop())

    def checkit(self, char):    
        if char == "(":
            self.stack.append(char)
        elif char == ")":
            while self.stack and self.stack[-1] != "(":
                self.output.append(self.stack.pop())
            if self.stack and self.stack[-1] == "(":
                self.stack.pop()
        else:
            while self.stack and self.dict[char] <= self.dict.get(self.stack[-1]):
                self.output.append(self.stack.pop())
            self.stack.append(char)

    def display(self):
        print("Postfix expression is:", " ".join(self.output))


# Run the program
a1 = Conversion()
a1.input()
  