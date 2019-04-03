# using heapq library to handle the priority Quee
# Heaps are binary trees for which every parent node has a value less than 
# or equal to any of its children

import heapq

class priorityQueue:
    def __init__(self):
        self.queue =[]
        self.index = 0
        
    def insert(self, priority, node):
        heapq.heappush(self.queue, (priority, self.index, node))
        self.index += 1
        
    def remove(self):
        return heapq.heappop(self.queue)[-1]
    
    
    def isEmpty(self):
        return (self.queue) == 0
    
"""
# Test cases
queue = priorityQueue()
queue.insert(1,a)
queue.insert(1, b)
queue.insert(13, c)
k = queue.remove()
print((k.q, k.r))
k = queue.remove()
print((k.q, k.r))
"""