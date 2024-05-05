class Heap:
    def __init__(self):
        self.data = []
    
    def root_node(self):
        if len(self.data) > 0:
            return self.data[0]
        return None
    
    def last_node(self):
        if len(self.data) > 0:
            return self.data[-1]
        return None
    
    def left_child_index(self, index):
        left_index = (index*2) + 1
 
        if left_index < len(self.data):
            return left_index
        return None
    
    def right_child_index(self, index):
        right_index = (index*2) + 2

        if right_index < len(self.data):
            return right_index
        return None
    
    def parent_index(self, index):
        parent = (index - 1) // 2
        if index > 0:
            return parent
        return None
    
    def insert(self, val):
        self.data.append(val)

        new_node_index = len(self.data) - 1

        while new_node_index > 0 and self.data[new_node_index] > self.data[self.parent_index(new_node_index)]:
            parent_index = self.parent_index(new_node_index)
            
            self.data[parent_index], self.data[new_node_index] = \
            self.data[new_node_index], self.data[parent_index]

            new_node_index = parent_index
    
    def delete(self):

        if len(self.data) == 0:
            return None
        
        if len(self.data) == 1:
            return self.data.pop()
        
        root_value = self.data[0]
        self.data[0] = self.data.pop()

        trickle_node_index = 0

        while self.has_greater_child(trickle_node_index):
            larger_child_index = self.calculate_larger_child_index(trickle_node_index)

            self.data[trickle_node_index], self.data[larger_child_index] = \
            self.data[larger_child_index], self.data[trickle_node_index]

            trickle_node_index = larger_child_index
        
        return root_value
    
    def has_greater_child(self, index: int) -> bool:
        left_child_index = self.left_child_index(index)
        right_child_index = self.right_child_index(index)
        has_left_child = left_child_index < len(self.data)
        has_right_child = right_child_index < len(self.data)
        return (has_left_child and self.data[left_child_index] > self.data[index]) or \
               (has_right_child and self.data[right_child_index] > self.data[index])
    
    def calculate_larger_child_index(self, index: int) -> int:
        left_child_index = self.left_child_index(index)
        right_child_index = self.right_child_index(index)
        if right_child_index < len(self.data) and \
           self.data[right_child_index] > self.data[left_child_index]:
            return right_child_index
        return left_child_index


