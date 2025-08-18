
from typing import Optional, Union, List
from collections import defaultdict

class graphNode:
    def __init__(self, value : Union[str, int] , connection_to :List ):
        self.value = value 
        self.connection_to = connection_to
         

    def __str__(self) -> str:
        return f"graphNode is created with {self.value} and {self.connection_to}"

class graph :
    def __init__(self) -> None:
        self.head = defaultdict(list)

    def add_tograph (self, value , connections):
        if not connections:
            self.head[value] = [] 
        elif value not in self.head:
            self.head[value] = []
            if isinstance(connections, list):
                for _i in connections:
                    self.head[value].append(_i)

            else:
                self.head[value].append(connections)

        else:
            if isinstance(connections, list):
                for _i in connections:
                    self.head[value].append(_i)

            else:
                self.head[value].append(connections)

    def remove_connection(self, value, connections):
        if value not in self.head:
            print(f"{value} not in the Graph")
            return  
        
        try:
            self.head[value].remove(connections)

        except ValueError:
            print(f"connection b/w {value} and {connections} is not established")

        finally:
            print(f"(exected)")
            return  

    def removeUnwantedMains (self):
        keys_to_remove = [k for k, v in self.head.items() if v is None or len(v) == 0]

        print(keys_to_remove)
        for _i in keys_to_remove:
            self.head.pop(_i)

        return
        
    def descgraph (self):
        return f"graph image : {dict(self.head)}"

cl = graph()
cl.add_tograph(1,3)
cl.add_tograph(1,4)
cl.add_tograph(2,3)
cl.add_tograph(2,1)
cl.add_tograph(3,1)
cl.remove_connection(3,1)
cl.remove_connection(3,1)
print(cl.descgraph())
cl.removeUnwantedMains()
print(cl.descgraph())
cl.add_tograph(3,[1,2,3,4,6])
print(cl.descgraph())

