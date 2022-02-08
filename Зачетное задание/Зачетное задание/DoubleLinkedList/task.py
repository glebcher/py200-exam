from collections.abc import MutableSequence
from typing import Any, Iterable, Optional
from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    def __init__(self, data: Iterable = None):
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

    def insert(self, index, value: Any) -> Node:
        head = self
        if index == 0:
            new_node = Node(value)
            new_node.next = self.head
            head = new_node
        else:
            while index != 0:
                index -= 1

                if index == 0:
                    new_node = Node(value)
                    new_node.next = self.head.next
                    self.head.next = new_node
                    break

                self.head = self.head.next
                if self.head is None:
                    break

            if index != 0:
                print("Индекс вне диапазона")

        self.len += 1
        return head

      # #current = self.step_by_step_on_nodes(index)
        # previous = self.step_by_step_on_nodes(index - 1)
        # new_node = Node(item)
        # not_last_node = Node(item, self.head.next)
        # if index == 0:
        #     self.head = new_node
        # elif index == self.len:
        #     self.append(item)
        # else:
        #     previous.next = new_node
        #     self.len += 1

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def __len__(self) -> int:
        return self.len

    def __delitem__(self, index: int):
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

    def __setitem__(self, index: int, value: Any):
        node = self.step_by_step_on_nodes(index)
        node.value = value


class DoubleLinkedList(LinkedList):
    def __init__(self, data: Iterable = None):
        super(LinkedList, self).__init__(data)
        self.len = 0
        self.head: Optional[DoubleLinkedNode] = None
        self.tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node

    def append(self, value: Any):
        append_node = DoubleLinkedNode(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1


if __name__ == "__main__":
    list_ = ([1, 2, 3])
    list2 = ([3, 5, 15])
    ll = LinkedList(list_)
    print(ll)

    print(ll.append(15), "добавили 15 в конец списка")
    print(ll.append(15), "добавили 15 в конец списка")
    print(ll.append(15), "добавили 15 в конец списка")
    print(ll)
    print(ll[3], "достаем элемент под индексом 3")
    print(ll.insert(1, 7), "добавили элемент 7 на индекс 1")
    # print(ll.insert(3, 8), "добавили элемент 8 на индекс 3")
    # print(ll.insert(2, 9), "добавили элемент 9 на индекс 2")
    # print(ll)
    # print(ll[1], "достаем элемент под индексом 1")
    # print(len(ll), "возвращаем длину списка")
    #print(repr(ll))
    #ll.step_by_step_on_nodes(3)




    # print(ll.insert(1, 7), "добавили элемент 7 на индекс 1")
    # print(ll, "возвращаем список")
    #print(ll.__getitem__(1), "достаем элемент под индексом 1")
    #print(ll.__len__(), "возвращаем длину списка после удаления")
    # print(ll)
    # print(ll)
