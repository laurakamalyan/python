class queue_priority:
    def __init__(self):
        self.__queue = []

    def add_item(self, item):
        self.__queue.append(item)

    def delete_item(self):
        while self.__queue:
            print(self.__queue.pop())

    def get_que(self):
        return self.__queue

    def sort_queue(self):
        self.__queue.sort(reverse=True)


queue1 = queue_priority()
queue1.add_item((2, "Adam"))
queue1.add_item((1, "John"))
queue1.add_item((3, "John"))
print(queue1.get_que())
queue1.sort_queue()
print(queue1.get_que())
queue1.delete_item()
