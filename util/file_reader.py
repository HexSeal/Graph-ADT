from graphs.graph import Graph


def read_graph_from_file(filename):
    """
    Read in data from the specified filename, and create and return a graph
    object corresponding to that data.

    Arguments:
    filename (string): The relative path of the file to be processed

    Returns:
    Graph: A directed or undirected Graph object containing the specified
    vertices and edges
    """

    # TODO: Use 'open' to open the file
    f = open(filename, "r")

    # TODO: Use the first line (G or D) to determine whether graph is directed 
    # and create a graph object
    lines = f.readlines()
    if lines[1] == "G":
        graph = Graph(False)
        
    elif lines[1] == "D":
        graph = Graph()
        
    else:
        print("Invalid Input")

    # TODO: Use the second line to add the vertices to the graph
    vertices = f.readline(lines[2])
    for _ in vertices:
        graph.add_vertex(_)

    # TODO: Use the 3rd+ line to add the edges to the graph
    for line in lines:
        if line > 2:
            curr = f.readlines(line)
            vert1 = f.readline(curr[1])
            vert2 = f.readline(curr[2])
            
            graph.add_edge(vert1, vert2)
            
    f.close()
    return graph

if __name__ == '__main__':
    graph = read_graph_from_file('test.txt')

    print(graph)