from graphs.graph import Graph, Vertex

class WeightedVertex(Vertex):
    def __init__(self, vertex_id):
        """
        Initialize a vertex and its neighbors.

        Parameters:
        vertex_id (string): A unique identifier to identify this vertex.
        """
        self.__id = vertex_id
        self.__neighbors_dict = {} # id -> (obj, weight)

    def add_neighbor(self, vertex_obj, weight):
        """
        Add a neighbor along a weighted edge by storing it in the neighbors dictionary.

        Parameters:
        vertex_obj (Vertex): An instance of Vertex to be stored as a neighbor.
        weight (int): The edge weight from self -> neighbor.
        """
        self.__neighbors_dict[vertex_obj.__id] = (vertex_obj, weight)
        return self.__neighbors_dict

    def get_neighbors(self):
        """Return the neighbors of this vertex as a list of neighbor ids."""
        return list(self.__neighbors_dict.values())

    def get_neighbors_with_weights(self):
        """Return the neighbors of this vertex as a list of tuples of (neighbor_id, weight)."""
        # TODO: Implement this function.
        pass


class WeightedGraph(Graph):
    def __init__(self, is_directed=True):
        """
        Initialize a weighted graph object with an empty vertex dictionary.

        Parameters:
        is_directed (boolean): Whether the graph is directed (edges go in only one direction).
        """
        self.__vertex_dict = {} # id -> object
        self.__is_directed = is_directed

    def add_vertex(self, vertex_id):
        """
        Add a new vertex object to the graph with the given key and return the vertex.

        Parameters:
        vertex_id (string): The unique identifier for the new vertex.

        Returns:
        Vertex: The new vertex object.
        """
        vertex = Vertex(vertex_id)
        self.__vertex_dict[vertex_id] = vertex
        return vertex

    def add_edge(self, vertex_id1, vertex_id2, weight):
        """
        Add an edge from vertex with id `vertex_id1` to vertex with id `vertex_id2`.

        Parameters:
        vertex_id1 (string): The unique identifier of the first vertex.
        vertex_id2 (string): The unique identifier of the second vertex.
        """
        vertex1 = self.get_vertex(vertex_id1)
        vertex2 = self.get_vertex(vertex_id2)
        
        # print("Vertex Id 1 {} Vertex Id 2 {}".format(vertex_id1, vertex_id2))
        vertex1.add_neighbor(vertex2, weight)
        
        if self.__is_directed == False:
            vertex2.add_neighbor(vertex1, weight)
    
    
    
    # Kruskal's Algorithm - Find Edges of a Minimum-Spanning Tree
    def union(self, parent_map, vertex_id1, vertex_id2):
        """Combine vertex_id1 and vertex_id2 into the same group."""
        vertex1_root = self.find(parent_map, vertex_id1)
        vertex2_root = self.find(parent_map, vertex_id2)
        parent_map[vertex1_root] = vertex2_root


    def find(self, parent_map, vertex_id):
        """Get the root (or, group label) for vertex_id."""
        if(parent_map[vertex_id] == vertex_id):
            return vertex_id
        return self.find(parent_map, parent_map[vertex_id])

    def minimum_spanning_tree_kruskal(self):
        """
        Use Kruskal's Algorithm to return a list of edges, as tuples of 
        (start_id, dest_id, weight) in the graph's minimum spanning tree.
        """
        # TODO: Create a list of all edges in the graph, sort them by weight 
        # from smallest to largest

        # TODO: Create a dictionary `parent_map` to map vertex -> its "parent". 
        # Initialize it so that each vertex is its own parent.

        # TODO: Create an empty list to hold the solution (i.e. all edges in the 
        # final spanning tree)

        # TODO: While the spanning tree holds < V-1 edges, get the smallest 
        # edge. If the two vertices connected by the edge are in different sets 
        # (i.e. calling `find()` gets two different roots), then it will not 
        # create a cycle, so add it to the solution set and call `union()` on 
        # the two vertices.

        # TODO: Return the solution list.
        
    
    
    # Prim's Algorithm - Find the weight of a MST
    def minimum_spanning_tree_prim(self):
        """
        Use Prim's Algorithm to return the total weight of all edges in the
        graph's spanning tree.

        Assume that the graph is connected.
        """
        # TODO: Create a dictionary `vertex_to_weight` and initialize all
        # vertices to INFINITY - hint: use `float('inf')`

        # TODO: Choose one vertex and set its weight to 0

        # TODO: While `vertex_to_weight` is not empty:
        # 1. Get the minimum-weighted remaining vertex, remove it from the
        #    dictionary, & add its weight to the total MST weight
        # 2. Update that vertex's neighbors, if edge weights are smaller than
        #    previous weights

        # TODO: Return total weight of MST
        
        
    
    # Dijkstra's Algorithm - Shortest Path
    def find_shortest_path(self, start_id, target_id):
        """
        Use Dijkstra's Algorithm to return the total weight of the shortest path
        from a start vertex to a destination.
        """
        # TODO: Create a dictionary `vertex_to_distance` and initialize all
        # vertices to INFINITY - hint: use `float('inf')`

        # TODO: While `vertex_to_distance` is not empty:
        # 1. Get the minimum-distance remaining vertex, remove it from the
        #    dictionary. If it is the target vertex, return its distance.
        # 2. Update that vertex's neighbors by adding the edge weight to the
        #    vertex's distance, if it is lower than previous.

        # TODO: Return None if target vertex not found.
        
        
        
    def floyd_warshall(self):
        """
        Return the All-Pairs-Shortest-Paths dictionary, containing the shortest
        paths from each vertex to each other vertex.
        """
        
        dist = {}
        vertex_ids = self.vertex_dict.keys()
        
        # Create a dictionary of all vertices and their possible connections
        for v1 in vertex_ids:
            dist[vertex1] = dict()
            for v2 in vertex_ids:
                dist[v1][v2] = WeightedGraph.INFINITY
            dist[v1][v1] = 0
        
        # Add all edge weights to the dict
        vertices = self.get_vertices()
        
        for vertex in vertices:
            weighted_neighbors = vertex.get_neighbors_with_weights()
            
            for neighbor, weight in weighted_neighbors:
                dist[vertex.get_id()][neighbor.get_id()] = weight
        
        for i in vertices:
            for j in vertices:
                for k in vertices:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    
        return dist