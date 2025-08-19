
from typing import List


class GraphNode :
    def __init__(self, value : int, connects_to : List = []) -> None :
        self.value = value 
        self.connects_to = []

    def __str__(self) -> str:
        return f"GraphNode is created with {self.value} and {self.connects_to}"


class Graph :
    def __init__(self) -> None:
        self.node = {}

    def addto_graph(self, value : int, connects_to : List[int]) -> None:
        if value not in self.node:
            
