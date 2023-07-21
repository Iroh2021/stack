class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def size(self):
        return len(self.stack)


def check_balance(string):
    stack = Stack()
    opening_brackets = "({["
    closing_brackets = ")}]"

    for char in string:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return "Несбалансированно"
            bracket = stack.pop()
            if opening_brackets.index(bracket) != closing_brackets.index(char):
                return "Несбалансированно"

    if stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"
if __name__ == '__main__':
    string = input("Введите строку со скобками: ")
    print(check_balance(string))