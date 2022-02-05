from collections.abc import MutableSequence
from typing import Any, Iterable, Optional
from node import Node


#class Abstract:
   # ...

    #@MutableSequence
    #def __init__(self, data: Iterable = None):
      #  ...
class LinkedList:
    def __init__(self, data: Iterable = None):
       # super().__init__()
        self.len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    def step_by_step_on_nodes(self, index: int) -> Node:
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        if left_node is not None:
            left_node.next = right_node

    def append(self, value: Any):
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

    def insert(self, index, item):

        current = self.head
        new_node = Node(item, None)
        if index == 0:
            self.__setitem__(index, item)
        elif index == self.len:
            self.append(item)
        else:
            current_node = 0
            while current.next is not None:

                if (index-1) == current_node:
                    current.setNext(new_node)

                if index == current_node:
                    new_node.setNext(current.next())
                current = current.next

                current_node += 1
            self.len += 1

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def __len__(self) -> int:
        return self.len

    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:
            raise IndexError()

        if index == 0:
            self.head = self.head.next
        elif index == self.len - 1:
            tail = self.step_by_step_on_nodes(index - 1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            del_node = prev_node.next
            next_node = del_node.next

            self.linked_nodes(prev_node, next_node)

        self.len -= 1

    def __getitem__(self, index: int) -> Any:
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        node = self.step_by_step_on_nodes(index)
        node.value = value


class DoubleLinkedList(LinkedList):
    def __init__(self, data: Iterable = None):
        super(LinkedList, self).__init__(data)
        self.len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node

    def append(self, value: Any):
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1


if __name__ == "__main__":
    list_ = ([1, 2, 3])

    ll = LinkedList(list_)
    print(ll)

    # print(ll.append(15), "добавили 15 в с конец списка")
    # print(ll.__getitem__(3), "достаем элемент под индексом 3")
    # print(ll.insert(1, 7), "добавили элемент 7 на индекс 1")
    # print(ll.__getitem__(1), "достаем элемент под индексом 1")
    # print(ll.__len__(), "возвращаем длину списка")
    # ll.step_by_step_on_nodes(3)
    # print(ll.__delitem__(2), "удаляем элемент по индексом 2")

    ll.remove(1)
    print("удаляем элемент под индексом 1")
    print(ll.insert(1, 7), "добавили элемент 7 на индекс 1")
    print(ll, "возвращаем список")
    #print(ll.__getitem__(1), "достаем элемент под индексом 1")
    #print(ll.__len__(), "возвращаем длину списка после удаления")
    # print(ll)
    # print(ll)
