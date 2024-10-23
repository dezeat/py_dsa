"""..."""

from __future__ import annotations

from pydantic.dataclasses import dataclass


@dataclass
class Node:
    """..."""

    value: int
    next: Node | None = None


@dataclass
class LinkedList:
    """..."""

    head: Node | None = None
    tail: Node | None = None
    length: int = 0
    current_node: Node | None = None

    def __len__(self) -> int:
        """..."""
        return self.length

    def __repr__(self) -> str:
        """..."""
        return " -> ".join([str(node.value) for node in self])

    def __iter__(self) -> LinkedList:
        """..."""
        self.current_node = self.head
        return self

    def __next__(self) -> Node:
        """..."""
        if self.current_node is not None:
            result = self.current_node
            self.current_node = self.current_node.next
            return result

        raise StopIteration

    def is_empty(self) -> bool:
        """..."""
        return self.length == 0

    def _reduce_length(self) -> None:
        """..."""
        self.length -= 1

    def _increase_length(self) -> None:
        """..."""
        self.length += 1

    def lookup_by_index(self, target: int) -> Node:
        """..."""
        if target < 0 or target >= self.length:
            msg = "Target index out of range"
            raise IndexError(msg)

        for index, node in enumerate(self):
            if index == target:
                return node

        msg = "This should never happen; index check is above."
        raise ValueError(msg)

    def lookup_by_value(self, value: int) -> list[int] | None:
        """..."""
        indices = [index for index, node in self if node.value == value]  # type: ignore  # noqa: PGH003
        return indices if indices else None

    def create_from_node(self, node: Node) -> None:
        """..."""
        self.head = self.tail = node
        self.tail.next = None
        self._increase_length()

    def insert_end(self, node: Node) -> None:
        """..."""
        if self.length == 0:
            self.create_from_node(node)

        else:
            self.tail.next = node  # type: ignore  # noqa: PGH003
            self.tail = node
            self.tail.next = None

        self._increase_length()

    def insert_start(self, node: Node) -> None:
        """..."""
        if self.length == 0:
            self.create_from_node(node)

        else:
            node.next = self.head
            self.head = node

        self._increase_length()

    def insert_at_index(self, node: Node, index: int) -> None:
        """..."""
        if index < 0 or index > self.length:
            msg = "Target index out of range"
            raise IndexError(msg)

        if self.length == 0:
            self.create_from_node(node)
            return

        if index == self.length:
            self.insert_end(node)
            return

        prev_node = self.lookup_by_index(index - 1)

        node.next = prev_node.next
        prev_node.next = node

        self._increase_length()

    def insert_after_node(self, target_node: Node, new_node: Node) -> None:
        """..."""
        if target_node in self.traverse():
            new_node.next = target_node.next
            target_node.next = new_node
            self._increase_length()
        else:
            msg = "Target node not found in list."
            raise ValueError(msg)

    def delete_node(self, node: Node) -> None:
        """..."""
        if node == self.head:
            self.delete_at_beginning()

        if node == self.tail:
            self.delete_at_end()

        for prev_node in self:
            if prev_node.next == node:
                prev_node.next = node.next
                node.next = None
                self._reduce_length()
                return

        msg = "Target node not found in list."
        raise ValueError(msg)

    def delete_at_index(self, index: int) -> None:
        """..."""
        if index < 0 or index > self.length - 1:
            msg = "Target index out of range"
            raise IndexError(msg)

        if index == 0:
            self.delete_at_beginning()
            return

        if index == self.length - 1:
            self.delete_at_end()
            return

        prev_node = self.lookup_by_index(index - 1)

        current_node = prev_node.next
        prev_node.next = current_node.next  # type: ignore  # noqa: PGH003
        current_node.next = None  # type: ignore  # noqa: PGH003

        self._reduce_length()

    def delete_at_beginning(self) -> None:
        """..."""
        if self.length == 0:
            msg = "Cannott remove node from empty list"
            raise IndexError(msg)

        self.head = self.head.next  # type: ignore  # noqa: PGH003
        self._reduce_length()

    def delete_at_end(self) -> None:
        """..."""
        if self.length == 0:
            msg = "Cannott remove node from empty list"
            raise IndexError(msg)

        prev_node = self.lookup_by_index(self.length - 2)
        self.tail = prev_node
        self.tail.next = None

        self._reduce_length()

    def traverse(self) -> list[Node]:
        """..."""
        return list(self)

    @classmethod
    def from_arr(cls, arr: list[int]) -> LinkedList:
        """..."""
        if not arr:
            msg = "Array needs to be non empty"
            raise ValueError(msg)

        head: Node
        tail: Node

        previous: Node | None = None

        for index, value in enumerate(arr):
            cls.length += 1
            current = Node(value)

            if previous:
                previous.next = current
            if index == 0:
                head = current
            if index == len(arr) - 1:
                tail = current

            previous = current

        return cls(head=head, tail=tail)
