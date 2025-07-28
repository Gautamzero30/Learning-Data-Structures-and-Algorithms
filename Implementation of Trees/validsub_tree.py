from collections import deque
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None      

def serialize(root):
    
    queue = deque()
    queue.append(root)
    output = []


    while queue:
        current = queue.popleft()
        
        if current is None:
            output.append("@")  
            continue  
        output.append(current.value)    
        queue.append(current.left)
        queue.append(current.right)

        
      
    return output
# def deserialize(output):

#     if not output or output == "@":
#         return None
#     i= 0
#     root = Node(output[i])
#     root.left   = deserialize(output[i+1])
#     root.right  = deserialize(output[i+2])
#     return root
    
    

if __name__ == "__main__":
    root = Node(5)
    root.left = Node(4)
    root.right = Node(3)
    root.left.left = Node(2)
    root.left.right = Node(1)

    serialized_output = serialize(root)
    print("Serialized output:", serialized_output)

    

    