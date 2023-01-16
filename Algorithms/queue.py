class Queue1:
    def __init__(self):
        self.__queue = []
        self.__index_item = 0
        self.__size = 0

    def enqueue(self, *items):
        for n in items:
            self.__queue.append(n)

    def dequeue(self):
        if not self.is_empty():
            return f"deleted item = {self.__queue.pop(self.__index_item)}"
        else:
            return "Empty"

    def size_queue(self):
        for i in self.__queue:
            self.__size += 1

        return f"size = {self.__size}"

    def is_empty(self):
        if self.size_queue == 0:
            return True

    def get_queue(self):
        return f"queue = {self.__queue}"


queue1 = Queue1()
queue1.enqueue(5, 8, 11, 3, 24)
print(queue1.get_queue())

print(queue1.dequeue())
print(queue1.get_queue())

print(queue1.size_queue())
