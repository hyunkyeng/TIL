class Stack:
    def __init__(self):
        self.items = []
    def empty(self):
        return not self.items
    def top(self):
        if self.items:
            return self.items[-1]
    def pop(self):
        if self.items:
            return self.items.pop()
    def push(self, elem):
        self.items.append(elem)


print(''.join(reversed('HI')))