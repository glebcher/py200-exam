from typing import Any, Optional


class Node:
    def __init__(self, value: Any,  next_: Optional["Node"] = None):
        self.value = value
        self.next = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    @staticmethod
    def is_valid(node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError
        elif Node is None:
            raise ValueError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_

    def setNext(self, next_node):
        self.next = next_node


class DoubleLinkedNode(Node):
    def __init__(self, value: Any, prev: Optional["Node"] = None,  next_: Optional["Node"] = None):
        super().__init__(value=value, next_=next_)
        self.prev = prev
    @property
    def prev(self):
        return self.prev() if self._prev else None

    @prev.setter
    def prev(self, prev_: Optional["Node"]):
        self.is_valid(prev_)
        self._prev = prev_

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        next_prev = None if self.prev is None else f"DoubleLinkedNode({self.prev})"
        next_repr = None if self.next is None else f"DoubleLinkedNode({self.next})"

        return f"DoubleLinkedNode({self.value}, {next_prev}, {next_repr})"


if __name__ == "__main__":
    ln = Node([1, 2, 3])
    dln = DoubleLinkedNode([1, 2, 3])
    print(ln)
    print(ln.__repr__)
    print(ln.__str__)
    print(dln.__repr__)
    print(dln.next)
    print(dln.prev)