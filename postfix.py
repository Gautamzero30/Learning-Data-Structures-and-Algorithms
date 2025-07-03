class postfix:
    def __init__(self):
        self.stack = []

    def enter(self):
        expression = input("Enter a postfix expression: ")
        self.evaluatepostfix(expression)    

    
    def evaluatepostfix(self,expression):
        if expression.strip() == "":
            print("Empty expression is not allowed.")
            return
        for char in expression.split():
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
                    
                    
                elif char == '**':
                    result = a ** b
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
e1= postfix()
e1.enter()

 




