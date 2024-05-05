
#Q4:
from collections import deque
class Vertex:

    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []
    
    def add_adjacent_vertices(self, vertex):
        self.adjacent_vertices.append(vertex)


def bfs_search(starting_vertex, search_value):
    queue = deque([])
    visited_vertices = {}
    visited_vertices[starting_vertex.value] = True

    queue.append(starting_vertex)
    # While the queue is not empty:
    while queue:
        # Remove the first vertex off the queue and make it the current vertex:
        current_vertex = queue.popleft()

        if current_vertex.value == search_value:
            return current_vertex
        # Print the current vertex's value:
        print(current_vertex.value)


        # Iterate over current vertex's adjacent vertices:
        for adjacent_vertex in current_vertex.adjacent_vertices:

            # If we have not yet visited the adjacent vertex:
            if not visited_vertices.get(adjacent_vertex.value, False):
            # Mark the adjacent vertex as visited:
                visited_vertices[adjacent_vertex.value] = True
                # Add the adjacent vertex to the queue:
                queue.append(adjacent_vertex)


#q5:

def degree_search(start_vertex, end_vertex, visited_vertices = {}):

    queue = deque([])

    previous_vertex_table = {}

    visited_vertices[start_vertex.value] = True
    queue.append(start_vertex)
    
    while queue:
        current_vertex = queue.popleft()
        
        for adjacent_vertex in current_vertex.adjacent_vertices:

            if adjacent_vertex.value not in visited_vertices:
                visited_vertices[adjacent_vertex.value] = True

                queue.append(adjacent_vertex)

                previous_vertex_table[adjacent_vertex.value] = current_vertex.value
    

    shortest_path = []

    current_vertex_value = end_vertex.value

    while current_vertex_value != start_vertex.value:
        shortest_path.append(current_vertex_value)
        current_vertex_value = previous_vertex_table[current_vertex_value]
    
    shortest_path.append(current_vertex_value)
    return shortest_path.reversed()



