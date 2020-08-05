##################################################
# Name : Onpinya Phokhahutthakosol
# Student ID : 62-010126-2026-1
# File name : 1.py
##################################################

# update : 05 Aug 2020
class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.root = None

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

def isOperator(alphabet):
    if (alphabet == '&' or alphabet == '+' or alphabet == '!' ):
        return True
    else:
        return False

