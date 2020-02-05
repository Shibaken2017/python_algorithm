from typing import Any


class Stack:
    class UnderFlow(Exception):
        pass

    class OverFlow(Exception):
        pass

    def __init__(self, size_limit):
        self.size_limit = size_limit
        self.stack = [None]*size_limit
        self.head = 0

    def is_full(self) -> None:
        if self.head == self.size_limit:
            return True
        else:
            return False

    def push(self, x: Any) -> None:
        if self.is_full():
            raise Stack.OverFlow
        self.stack[self.head] = x
        self.head += 1

    def is_empty(self) -> None:
        if self.head == 0:
            return True
        else:
            return False

    def pop(self) -> Any:
        if self.is_empty():
            raise Stack.UnderFlow
        else:
            self.head -= 1
            return self.stack[self.head]
