class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def size(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.next

        return size

    def push_back(self, data):
        # if list is empty
        if self.head is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last.next.prev = self.last
            self.last = self.last.next

    def push_front(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = Node(data)
            self.last = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert(self, data, index):
        new_node = Node(data)
        current_node = self.head
        size = self.size()

        # if list is empty
        if self.head is None:
            self.head = new_node
            self.last = self.head

        # if want add in first
        if index == 0:
            self.push_front(data)
            return
        elif index > size:  # if want add in end
            self.push_back(data)
            return

        # in other cases
        for i in range(size):
            if i == index - 1:
                temp = current_node.next
                current_node.next.prev = new_node
                current_node.next = new_node

                new_node.prev = current_node
                new_node.next = temp
                break
            current_node = current_node.next

    # remove node by index
    def remove(self, index):
        current_node = self.head
        size = self.size()

        for i in range(size):
            if i == index - 1:
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
                break
            current_node = current_node.next

    def pop_back(self):
        current_node = self.head
        size = self.size()
        for i in range(0, size):
            if i == size - 2:
                self.last = current_node
                current_node.next.prev = None
                current_node.next = None
                return
            current_node = current_node.next

    def pop_front(self):
        self.head = self.head.next
        self.head.prev = None

    # remove all nodes
    def dispose(self):
        current_node = self.head
        while current_node is not None:
            temp = current_node.next
            current_node.prev = None
            current_node.next = None
            current_node = temp

        self.head = None
        self.last = None

    # find data by index
    def find(self, index):
        current = self.head
        size = self.size()
        for i in range(size):
            if index == i:
                return current.data
            current = current.next

    # find data index
    def search(self, data):
        current_node = self.head
        i = 0
        while current_node is not None:
            if current_node.data == data:
                return i
            current_node = current_node.next
            i += 1

        return "No such data."

    def show(self):

        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

        print()
        # from end to start
        current = self.last
        while current:
            print(current.data, end=" ")
            current = current.prev

    def get_next_node(self, n):
        current_node = self.head

        while current_node.next is not None:
            if current_node.data == n:
                return current_node.next.data
            current_node = current_node.next

        return "No next node."

    def get_previous_node(self, n):
        current_node = self.last

        while current_node.prev is not None:
            if current_node.data == n:
                return current_node.prev.data
            current_node = current_node.prev

        return "No previous node."


# from start to end
def show_list(n):
    for i in range(n.size()):
        print(n.find(i), end=" ")


# from end to start
def show_reverse_list(n):
    for i in range(n.size() - 1, -1, -1):
        print(n.find(i), end=" ")


node = DoubleLinkedList()
node.push_back(5)
node.push_back(6)
node.push_back(8)
node.push_back(9)
show_list(node)
