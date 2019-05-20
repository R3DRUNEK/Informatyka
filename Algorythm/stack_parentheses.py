class Stack:
    def __init__(self):
        self.s = []

    def push(self, item):
        self.s.append(item)

    def pop(self):
        self.s.pop()

    def isEmpty(self):
        return self.s == []

    def peek(self):
        return self.s[len(self.s)-1]

    def size(self):
        return len(self.s)


def parseParantheses(par):
    s = Stack()
    check = True
    for x in par:
        if x in '([{':
            s.push(x)
        else:
            if s.isEmpty():
                check = False
            else:
                s.pop()
