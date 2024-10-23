from pydantic.dataclasses import dataclass

@dataclass
class Node:
    value: int
    next: "Node" | None = None

@dataclass
class LinkedList:
    head: Node
    tail: Node


