from collections import deque

def POL_helper():
    print("File Imported")

# Part 1: DAG2UG
def convertDAGToUG(dag_graph:dict) -> dict:
    ''' This function returns a directed version of an inputted graph (i.e. each undirected edge in dag_graph is made to go in both directions).
    :param dag_graph: (dict) a graph with undirected edges
    :return : (dict) a graph with directed edges
    
    >>> convertDAGToUG({'you': ['alice', 'bob'], 'bob': ['peggy'], 'alice': ['claire'], 'claire': ['tom', 'jonny'], 'peggy': [], 'tom': [], 'jonny': []})
    {'you': ['alice', 'bob'], 'alice': ['you', 'claire'], 'bob': ['you', 'peggy'], 'peggy': ['bob'], 'claire': ['alice', 'tom', 'jonny'], 'tom': ['claire'], 'jonny': ['claire']}
    '''
    ret_dict: dict[str, list] = {}
    for node in dag_graph:
        for neighbor in dag_graph[node]:
            add_edge(ret_dict, node, neighbor)
    return ret_dict
 
def add_edge(graph:dict, node1:str, node2:str) -> None:
    ''' Adds an undirected edge between two nodes in an inputted graph if no edge exists.
    :param graph: (dict) The graph an edge should be added to.
    :param node1: (str) The first node that should have added edges.
    :param node2: (str) The second node that should have added edges.
    
    >>>add_edge({'a':[], 'b':[]}, "a", "b")
    graph becomes {'a':['b'], 'b':['a']}
    
    >>>add_edge({'a':['b'], 'b':[]}, "a", "b")
    graph becomes {'a':['b'], 'b':['a']}
    
    >>>add_edge({'a':[], 'b':['a']}, "a", "b")
    graph becomes {'a':['b'], 'b':['a']}
    '''
    if node1 not in graph:
        graph[node1] = [0] * 0 #empty array for node1 neighbors
    if node2 not in graph:
        graph[node2] = [0] * 0 #empty array for node2 neighbors
    if edge_exists(graph[node1], node2) is not True:
        graph[node1] = append(graph[node1], node2)
    if edge_exists(graph[node2], node1) is not True:
        graph[node2] = append(graph[node2], node1)
 
def edge_exists(arr:list, node:str) -> bool:
    ''' Checks if a list contains a specified node.
    :param arr: (list) the array that should be checked.
    :param node: (str) the node that may or may not be in the list.
    :return : (bool) true if a list contains an inputted string and false if it doesn't.
    
    >>> edge_exists(['a', 'b', 'c'], 'd')
    False
    >>> edge_exists(['a', 'b', 'c'], 'a')
    True
    '''
    for i in range(len(arr)):
        if arr[i] is node:
            return True
    return False

def append(arr:list, val:str) -> list:
    ''' Resizes and adds a node to the end of an array, returning the new array.
    :param arr: (list) the array that has to be resized.
    :param val: (str) the node that should be added to the end of the array
    :return : (list) the new list, containing all the same elements of arr with the addition of val at the end.
    
    >>> append({}, "a")
    {"a"}
    >> append({"a"}, "b")
    {"a", "b"}
    '''
    new_arr:list[str|None] = [None] * (len(arr) + 1)
    for i in range(len(arr)):
        new_arr[i] = arr[i]
    new_arr[len(arr)] = val
    return new_arr

def remove(arr:list) -> list:
    ''' Resizes and removes the final node of an array.
    :param arr: (list) the array that has to be resized.
    :return : (list) the new list, containing all the same elements of arr but without the final element

    >>>remove({"a"}, "a")
    {}
    '''
    new_arr:list[str|None] = [None] * (len(arr) - 1)
    for i in range(len(new_arr)):
        new_arr[i] = arr[i]
    return new_arr
 
# Part 2: BFS            
def findBFSPath(graph:dict, start_node:str, end_node:str) -> list:
    ''' Finds the shortest path between two nodes in a graph.
    :param graph: (dict) the graph to be searched
    :param start_node: (str) the start of the path
    :param end_node: (str) the end of the path
    :return : (list) list containing the shortest path between two nodes, or an empty list if no such path exists 

    dag1graph={'you': ['alice', 'bob'], 'bob': ['peggy'], 'alice': ['claire'], 'claire': ['tom', 'jonny'], 'peggy': [], 'tom': [], 'jonny': []}
    >>> findBFSPath(dag1graph, "jonny", "you")
    []
    >>> findBFSPath(dag1graph, "you", "jonny")
    ['you', 'alice', 'claire', 'jonny']
    '''
    if start_node==None or end_node==None:
        return []
    if start_node==end_node:
        return [start_node]
    
    prev: dict[str, list|None] = {}
    queue: list = [0] * len(graph)
    front: int = 0
    back: int = 0
    
    queue[back] = start_node
    back+=1
    prev[start_node] = None
    
    while front<back:
        current_node = queue[front]
        front+=1
        
        for child in graph.get(current_node, []):
            if child not in prev:
                prev[child] = current_node
                queue[back] = child
                back+=1
                
                if child is end_node:
                    return reconstructPath(prev, end_node)
    return []

def reconstructPath(prev:dict, end) -> list:
    ''' Creates a reversed list of a section of keys in a dictionary.
    :param prev: (dict) the dictionary we need the reversed keys of.
    :param end: () the final necessary node
    :return : (list) the reversed list of keyes
    
    prev = {'you': None, 'alice': 'you', 'bob': 'you', 'claire': 'alice', 'peggy': 'bob', 'tom': 'claire', 'jonny': 'claire'}
    >>>reconstructPath(prev, "jonny")
    ['you', 'alice', 'claire', 'jonny']
    '''
    path: list = []
    current = end
    
    while current is not None:
        path = append(path, current)
        current = prev[current]
    
    #Reverse the array
    rev_path = [0] * len(path)
    for i in range(len(path)):
        rev_path[len(path) - i - 1] = path[i]
    path=rev_path
    return path


# Part 3: ISCYCLIC
def isCyclic(graph:dict) -> bool:
    ''' Checks if an inputted graph includes cycles.
    :param graph: (dict) the graph that will be checked
    :return : (bool) False if there are no cycles, True otherwise. Inherently all undirected graphs will return True

    >>> isCyclic({})
    False
    isCyclic({'you':['alice'], 'alice': ['you']})
    True
    isCyclic({'you':[], 'alice': []})
    False
    graph1 = {'you': ['alice', 'bob'], 'alice': ['you', 'claire'], 'bob': ['you', 'peggy'], 'peggy': ['bob'], 'claire': ['alice', 'tom', 'jonny'], 'tom': ['claire'], 'jonny': ['claire']}
    >>> isCyclic(graph1)
    True
    '''
    
    #Maybe use fast and slow pointers?
        #Can't find a way that would work with dictionaries. Using DFS
        
    if len(graph)==0: #can't have a cycle if there are no nodes to create a cycle
        return False
    
    visited: list = []
    for node in graph.keys():
        if not edge_exists(visited, node):
            if dfs(graph, node, visited, []):
                return True
    return False

def dfs(graph:dict, node, visited, rec_stack) -> bool:
    ''' 
    :param graph: (dict)
    :param node: ()
    :param visited: (list)
    :rec_stack: (list)
    :return : (bool)

    >>>
    '''
    visited=append(visited, node)
    rec_stack=append(rec_stack, node)
    
    for child in graph.get(node, []):
        if not edge_exists(visited, child):
            if dfs(graph, child, visited, rec_stack):
                return True
        if edge_exists(rec_stack, child):
            return True
    
    rec_stack = remove(rec_stack)
    return False

# Part 4: ISCONNECTED
def isConnected(graph:dict) -> bool:
    ''' Checks  if there is a path between each node in a directed graph.
    :param graph: (dict) the graph to be checked
    :return : (bool) True if the nodes of the graph are connected, false if they are not

    >>> isConnected({}):
    True
    >>> isConnected({'a':['b'], 'b':['a']})
    True
    >>> isConnected({'a':['b'], 'b':['a'], 'c':[]})
    False
    '''
    if len(graph)==0 or len(graph)==1: #there can't be a disconnected node if there's no node to be disconnected from
        return True
    
    visited: dict[str, bool] = {}
    for node in graph:
        visited[node] = False
    
    start = next(iter(graph))
    queue = [0] * len(graph)
    front: int = 0
    back: int = 0
    
    # Enqueue the start node
    queue[back] = start
    back += 1
    visited[start] = True
    
    while front < back:
        # Dequeue the next node
        current_node = queue[front]
        front += 1
        
        # Visit each neighbor of the current node
        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue[back] = neighbor
                back += 1
    for node in visited:
        if not visited[node]:
            return False
    return True


# Part 5: TOPOSORT
def topoSort(graph:dict) -> list:
    ''' Computes a topological ordering of the nodes in a directed acyclic graph
    :param graph: (dict) A dictionary representing the DAG where keys are nodes and values are lists of nodes representing edges to neighbors.
    :return : (list) A list of nodes in topological order.

    >>> dag = {"a": ["b", "c"], "b": ["d"], "c": ["d"]}
        >>> topoSort(dag)
        ["a", "b", "c", "d"] or ["a", "c", "b", "d"]
    '''
    
    visited = {node: False for node in graph}
    result:deque = deque()
    
    for node in graph:
        if not visited[node]:
            topoDFS(visited, graph, result, node)
    
    return list(result)

def topoDFS(visited:dict, graph:dict, result:deque, node:str):
    '''
    :param visited: (dict)
    :param graph: (dict)
    :param result: (deque)
    :param node: (str)
    
    >>> topoDFS()
    '''
    visited[node] = True
    for neighbor in graph.get(node, []):
        if not visited[neighbor]:
            topoDFS(visited, graph, result, neighbor)
    result.appendleft(node)
