from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.current_num_of_node = 0
        self.key_value_entries = DoublyLinkedList()
        self.storage = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # for k in key:
        #     print(k.values, "the key, and value")
        # value = self.storage[key]
        # while self.current_num_of_node < self.limit:
        if key in self.storage:
            key_value = self.storage[key]
            # self.current_num_of_node += 1
            self.key_value_entries.move_to_end(key_value)
            return key_value.value[1]
        else:
            return None

        # pass

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # # if not limit
        # if not self.limit:
        #     # increament current_num_of_node
        #     self.current_num_of_node += 1
        #     # push key-value pair to dict and to the head of key_value_entries
        #     self.storage.update({key, value})
        #     self.key_value_entries.add_to_head(value)
        # # else
        # else:
        #     # pop from the dict and remove from the tail of key_value_entries
        #     self.current_num_of_node += 1
        #     self.storage.pop(key, None)
        #     self.key_value_entries.remove_from_tail()

        # # if key exist in the dict
        #     # replace value of key to new value of the key
        # # else
        #     # crete new node with and add to dict and to the head of key_value_entries

        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.key_value_entries.move_to_end(node)
            return

        if self.current_num_of_node == self.limit:
            del self.storage[self.key_value_entries.head.value[0]]
            self.key_value_entries.remove_from_head()
            self.current_num_of_node -= 1

        self.key_value_entries.add_to_tail((key, value))
        self.storage[key] = self.key_value_entries.tail
        self.current_num_of_node += 1
