class Calculator:
    def __init__(self, op, x, y):
        self.__result = ""
        self.__op = op
        self.__x = x
        self.__y = y

    def addition(self):
        self.__result = f"{self.__x} + {self.__y} = {self.__x + self.__y}"

    def subtraction(self):
        self.__result = f"{self.__x} - {self.__y} = {self.__x - self.__y}"

    def multiplication(self):
        self.__result = f"{self.__x} * {self.__y} = {self.__x * self.__y}"

    def division(self):
        if self.__y == 0:
            print("Error. Cannot divide by zero.")
            return
        self.__result = f"{self.__x} / {self.__y} = {self.__x / self.__y}"

    def get_result(self):
        match self.__op:
            case "+": self.addition()
            case "-": self.subtraction()
            case "*": self.multiplication()
            case "/": self.division()
        return self.__result


operation1 = Calculator('/', 8, 5)
print(operation1.get_result())
