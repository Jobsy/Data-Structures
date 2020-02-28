from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value == None:
            self.value = value
        elif value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target < self.value:
            if target == self.left.value:
                return True
            else:
                self.left.insert(target)
                return False
        elif target >= self.value:
            if target == self.right.value:
                return True
            else:
                self.right.insert(target)
                return False

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        # else:
        #     cb(self.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # stack = Stack()
        # stack.push(node)
        # print(stack.len(), "length")
        # print(node, "node")
        # # print(node.value, "node.value")
        # print(self.value, "self.value")
        # print(self.left, "self.left")
        # print(self.right.value, "self.right.value")
        if node == None:
            return
        if node.left:
            node.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.in_order_print(node.right)
        # print(node.value)
        # if self.left:
        #     print("LHS1")
        #     if self.left.value < self.value:
        #         print("LHS2")
        #         self.left.in_order_print(self.value)
        #     else:
        #         stack.push(self.value)
        #         print(self.left.value, "LHS3")
        # elif not self.left and self.right:
        #     stack.push(self.value)
        #     BinarySearchTree(value)
        # elif self.right:
        #     print("RHS1")
        #     if self.right.value >= self.value:
        #         stack.push(node.value)
        #         print(self.right.value, "RHS2")

        #     else:
        #         print("RHS3")
        #         self.right.in_order_print(node.value)

        # if node.value < self.value:
        #     if node.value == self.left.value:
        #         print(node.value)
        #     else:
        #         return self.left.in_order_print(node.value)
        #         # return False
        # elif node.value >= self.value:
        #     if node.value == self.right.value:
        #         print(node.value)
        #     else:
        #         return self.right.in_order_print(node.value)
        # return False

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        # print(stack.len(), "/////")
        # print(node, "node")
        # print(self, "self")

        while stack.len() > 0:
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        if node is None:
            return
        print(node.value)
        if node.left:
            node.pre_order_dft(node.left)
        if node.right:
            node.pre_order_dft(node.right)
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is None:
            return

        if node.left:
            node.post_order_dft(node.left)
        if node.right:
            node.post_order_dft(node.right)
        print(node.value)
