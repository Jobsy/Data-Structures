from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

# new_d_linked_list = doubly_linked_list


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # DoublyLinkedList.add_to_head(self, value)
        self.size += 1
        self.storage.add_to_head(value)

    def dequeue(self):
        if self.storage.length == 0:
            return None

        self.size -= 1
        return self.storage.remove_from_tail()

    def len(self):
        return self.size