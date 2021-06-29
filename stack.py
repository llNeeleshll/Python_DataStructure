from collections import deque

class Stack:

    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)

def split_word(word):
    return [char for char in word]

def reverse_string(str):

    stack = Stack()
    rev_str = ""

    arr_str = split_word(str)

    for item in arr_str:
        stack.push(item)

    while stack.size() > 0:
        rev_str += stack.pop()
    
    return rev_str

def check_brackets(str):

    stack = Stack()
    rev_str = ""

    arr_str = split_word(str)

    curly = 0
    square = 0
    circular = 0

    for item in arr_str:

        if item == "{":
            curly += 1
        elif item =="[":
            square += 1
        elif item == "(":
            circular += 1
            
        stack.push(item)

    while stack.size() > 0:

        item = stack.pop()

        if item == "}":
            curly -= 1
        elif item =="]":
            square -= 1
        elif item == ")":
            circular -= 1

    return curly == 0 and square == 0 and circular == 0




#print(reverse_string('I am awesome neelesh vishwakarma'))

# check for brackets
print(check_brackets('['))