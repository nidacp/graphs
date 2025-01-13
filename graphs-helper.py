from graphs import *

def getSmallDirectedExample() -> dict:
    graph = {}
    graph["you"] = ["alice", "bob"]
    graph["bob"] = ["peggy"]
    graph["alice"] = ["claire"]
    graph["claire"] = ["tom", "jonny"]
    graph["peggy"] = []
    graph["tom"] = []
    graph["jonny"] = []
    return graph

def getSmallDirectedExample2() -> dict:
    graph = {}
    graph["you"] = ["alice", "bob"]
    graph["bob"] = ["rando"]
    graph["alice"] = ["claire"]
    graph["claire"] = ["rando"]
    graph["rando"] = []
    graph["peggy"] = ["tom"]
    graph["tom"] = ["jonny"]
    graph["jonny"] = ["peggy"]
    return graph

def main():
    POL_helper()
    dag_graph1 = getSmallDirectedExample()
    undirected1 = convertDAGToUG(dag_graph1)
    dag_graph2 = getSmallDirectedExample2()
    undirected2 = convertDAGToUG(dag_graph2)
    print(dag_graph1)
    print(undirected1)
    print("TESTING BFSPATH.")
    print("Path between jonny and you is: ", findBFSPath(dag_graph1, "jonny", "you"))
    print("Path between you and johnny is: ", findBFSPath(undirected1, "you", "jonny"))
    print("Path between you and johnny is: ", findBFSPath(dag_graph2, "you", "jonny"))
    #When there's multiple paths, add a test case seeing if the shorter one is returned
    print("Path between you and rando is: ", findBFSPath(undirected2, "you", "rando"))
    print("TESTING IS CYCLIC.")
    print("Should return False. Returns ", isCyclic(dag_graph1))
    print("Should return True. Returns ", isCyclic(undirected1))
    print("Should return True. Returns ", isCyclic(dag_graph2))
    print("Should return True. Returns ", isCyclic(undirected2))
    print("TESTING ISCONNECTED.")
    print("Should return True. Returns ", isConnected(dag_graph1))
    print("Should return True. Returns ", isConnected(undirected1))
    print("Should return False. Returns ", isConnected(dag_graph2))
    print("Should return False. Returns ", isConnected(undirected2))
    print("TESTING TOPOSORT.")
    print("before: ", list(dag_graph1.keys()))
    print("after: ", topoSort(dag_graph1))
    tinyDAG = {}
    tinyDAG["a"] = ["b", "c"]
    tinyDAG["b"] = ["d"]
    tinyDAG["c"] = ["d"]
    tinyDAG["d"] = []
    print(topoSort(tinyDAG))


if __name__ == "__main__":
    main()
