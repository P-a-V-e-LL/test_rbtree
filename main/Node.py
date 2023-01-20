import os
from termcolor import colored


class Node:
    def __init__(self, key):
        self.key = key
        self.red = True
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1

    def print_node(self):
        if self.red:
            print("{0}|{1}".format(colored(self.key, 'red'), self.size))
        else:
            print("{0}|{1}".format(self.key, self.size))

    def fix(self):
        if self.right != None and self.left != None:
            self.size = self.right.size + self.left.size + 1
        elif self.right == None and self.left != None:
            self.size = self.left.size + 1
        elif self.right != None and self.left == None:
            self.size = self.right.size + 1
