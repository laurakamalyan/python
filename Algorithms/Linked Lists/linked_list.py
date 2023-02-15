class Node:
    # constructor create a new node
    def __init__(self, data, n=None):
        self.data = data
        self.next = n


class LinkedList:
    def __init__(self):
        self.head = None # first node in list
        self.last_node = None # last node in list

    def size(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count

    def push_back(self, data):
        # if list is empty
        if self.head is None:
            self.head = Node(data)
            self.last_node = self.head # only one element so the last also refer to the first
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def push_front(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.last_node = self.head
        else:
            new_node.next = self.head
            self.head = new_node

    def insert(self, data, index):
        new_node = Node(data)
        current_node = self.head
        size = self.size()

        # if list is empty
        if self.head is None:
            self.head = new_node
            self.last_node = self.head

        # if want add in first
        if index == 0:
            self.push_front(data)
            return
        elif index > size: # if want add in end
            self.push_back(data)
            return

        # in other cases
        i = 0
        while current_node is not None:
            if index - 1 == i:
                temp = current_node.next
                current_node.next = new_node
                new_node.next = temp
                break
            else:
                current_node = current_node.next
                i += 1

    # remove node by index
    def remove(self, index):
        current_node = self.head
        i = 0
        while current_node is not None:
            if index - 1 == i:
                current_node.next = current_node.next.next
                break
            else:
                current_node = current_node.next
                i += 1

    def pop_back(self):
        current_node = self.head
        size = self.size()
        for i in range(0, size):
            if i == size - 2:
                current_node.next = None
                self.last_node = current_node
                return
            current_node = current_node.next

    def pop_front(self):
        self.head = self.head.next

    # remove all nodes
    def dispose(self):
        current_node = self.head
        while current_node is not None:
            current_node.next = None
            current_node = current_node.next

        self.head = None

    # find data by index
    def find(self, index):
        current_node = self.head
        size = self.size()
        for i in range(size):
            if index == i:
                return current_node.data
            current_node = current_node.next

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

    # get next node
    def get_next_node(self, n):
        current_node = self.head
        size = self.size()

        for i in range(0, size - 1): # size-1 because the last node has no next node
            if current_node.data == n:
                return current_node.next.data
            current_node = current_node.next

        return "No next node."

    # get max element
    def max(self):
        current_node = self.head
        max_node = self.head
        while current_node:
            if current_node.data > max_node.data:
                max_node = current_node
            current_node = current_node.next

        return max_node.data

    # get min element
    def min(self):
        current_node = self.head
        min_node = self.head
        while current_node:
            if current_node.data < min_node.data:
                min_node = current_node
            current_node = current_node.next

        return min_node.data


def show_list(n):
    for i in range(n.size()):
        print(n.find(i), end=" ")


node = LinkedList()
node.push_back(42)
node.push_back(16)
node.push_back(88)
node.push_back(7)

show_list(node)
