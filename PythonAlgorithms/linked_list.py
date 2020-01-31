from typing import Any, Type


class Node:
    def __init__(self, data: Any = None, next: Node = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self,) -> None:
        self.no = 0
        self.head = None
        self.current = None

    def __len__(self) -> int:
        return self.no

    def search(self, data: Any) -> int:
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool:
        return self.search(data) >= 0

    def add_last(self, data: Any):
        if self.head is None:
            self.add_first(data)
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data, None)
            self.no += 1

    def remove_first(self) -> None:
        if self.head is not None:
            self.head = self.current = self.head.next
        self.no -= 1

    def remove_last(self):
        if self.head is not None:
            if self.head.next is None:
                self.remove_first()
            else:
                ptr = self.head
                pre = self.head

                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next
                # remove by assinning None
                pre.next = None
                self.current = pre
                self.no -= 1

    def remove(self, p: None) -> None:
        if self.head is not None:
            if p is self.head:
                self.remove_first()
            else:
                ptr = self.head
                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return
                # p is removed by skipping p which is next to ptr.next
                ptr.next = p.next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        self.remove(self.current)

    def clear(self) -> None:
        while self.head is not None:
            self.remove_first()
        self.current = None
        self.no = 0

    def next(self) -> bool:
        if self.current is None or self.current.next is None:
            return False
        self.currrent = self.current.next
        return True

    def print_current_node(self) -> None:
        if self.currren is None:
            print("current is not exist")
        else:
            print(self.current.data)

    def print(self) -> None:
        ptr = self.head
        while ptr is not None:
            print(ptr.next)
            ptr = ptr.next
