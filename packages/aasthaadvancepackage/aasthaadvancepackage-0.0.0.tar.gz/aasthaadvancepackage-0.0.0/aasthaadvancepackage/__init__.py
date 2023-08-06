class ArithmeticOperation:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def fact(self, n):
        f = 1
        if n < 0:
            print("Sorry Factorial is not allowed for negative number")
        elif n == 0:
            print("The factorial of 0 is 1")
        else:
            for i in range(1, n + 1):
                f *= i
            print("Factorial is:", f)






            