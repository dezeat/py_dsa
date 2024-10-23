from pydantic.dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: int
    next: Optional["Node"] | None = None


@dataclass
class LinkedList:
    head: Node
    tail: Node

    @classmethod
    def from_arr(cls, arr: list[int]) -> "LinkedList":
        head: Node | None = None
        tail: Node | None = None

        previous: Node | None = None

        for index, value in enumerate(arr):
            current = Node(value)

            if previous:
                previous.next = current

            if index == 0:
                head = current

            if index == len(arr) - 1:
                tail = current

            previous = current

        return cls(head=head, tail=tail)


ll = LinkedList.from_arr([1, 2, 3, 4, 5])
