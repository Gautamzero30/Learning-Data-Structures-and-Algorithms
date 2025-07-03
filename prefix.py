class prefix:
    def __init__(self):
        self.stack = []

    def enter(self):
        expression = input("Enter a prefix expression: ")
        if expression.strip() == "":
            print("Empty expression is not allowed.")
            return
        self.evaluateprefix(expression)    

    
    def evaluateprefix(self,expression):
        for char in reversed(expression.split()):
            if char.isdigit():
                self.stack.append(int(char))

            else:
                if len(self.stack) < 2:
                    print("at leat two operands in necessary for operation")
                    return
                b = self.stack.pop()
                a = self.stack.pop()

                if char == '+':
                    result = a + b
                elif char == '-':
                    result = a - b
                elif char == '*':
                    result = a * b
                elif char == '/':
                    if b == 0:
                        print("not possible, Division by zero.")
                        return
                    result = a / b
                else:
                    print(f" Unknown operator '{char}'.")
                    return

                self.stack.append(result)

        if len(self.stack) == 1:    
            print("Result:", self.stack.pop())
        else:
            print("Some thing is wrong in your expression")
e1= prefix()
e1.enter()

 




