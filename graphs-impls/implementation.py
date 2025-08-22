from typing import List, Union 
import time
from collections import defaultdict

class graphNode :
    def __init__(self, value : int, connections_to : Union[List, int] = []) -> dict:
        self.value = value 
        self.connections_to = connections_to
        pass

    def __str__(self) -> str:
        return "created"

class Graph :
    def __init__(self) -> None:
        self.nodes = {}
        pass


    def addtoGraph (self, value : int, conections : Union[List, int, None] = None) -> None:
        if value not in self.nodes:
            self.nodes[value] = [] 
            if isinstance(conections, list):
                self.nodes[value] = conections 

            elif isinstance(conections, int):
                self.nodes[value].append(conections)
            else:
                pass 

        else:
            if isinstance(conections, list):
                self.nodes[value].extend(conections)
            elif isinstance(conections, int):
                self.nodes[value].append(conections)
            else:
                pass 

        return 

    def desc(self) -> None:
        print(f"graph image : {self.nodes}")
        for i in range(10, -1, -1):
            print(f"\rcoundown :: {i}", end ="", flush=True)
            time.sleep(1)



cl = Graph() 
cl.addtoGraph(1, [2,3,4,5])
cl.addtoGraph(2, 5)
cl.addtoGraph(5, [4,2])
cl.addtoGraph(4, [12,4])
cl.addtoGraph(7, [625])
cl.desc()



