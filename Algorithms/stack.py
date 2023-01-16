class Stack:
    def __init__(self):
        self.__stack = []
        self.__maximum = 0

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        if len(self.__stack) == 0:
            return "Empty"
        else:
            return f"deleted item = {self.__stack.pop()}"

    def get_stack(self):
        return f"stack = {self.__stack}"

    def max_item(self):
        self.__maximum = self.__stack[0]
        for i in range(1, len(self.__stack)):
            if self.__stack[i] > self.__maximum:
                self.__maximum = self.__stack[i]
        return f"max = {self.__maximum}"


stack = Stack()
stack.push(6)
stack.push(8)
print(stack.get_stack())

print(stack.max_item())

stack.push(2)
print(stack.get_stack())
print(stack.pop())
print(stack.get_stack())
