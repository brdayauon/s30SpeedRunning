class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
"""
    removing node! not remove last. because what if we need to remove node.
    
    - in get function: 
        - if key in self.hm. we have to remove node first then add to head. then return value
    
    - in put function: 
        - make sure to get the node first instead of just calling self.hm[key]
        - then change the value -> remove -> addToHead
        
        if key not in self.hm:
            - put key/value in hashmap.
            - addToHead
            # check if go over capacity. 
                - get the last node
                - get the key
                - remove the node and del the key
"""
    
class LRUCache:
    
    def addToHead(self, node):
        node.next = self.head.next 
        node.next.prev = node
        self.head.next = node 
        self.head.next.prev = self.head 
    
    def removeNode(self, node):
        node.next.prev = node.prev 
        node.prev.next = node.next
        
    
    def __init__(self, capacity: int):
        self.hm = {} # {node:location}
        self.capacity = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail 
        self.tail.prev = self.head 
        
    def get(self, key: int) -> int:
        if key in self.hm:
            self.removeNode(self.hm[key])
            self.addToHead(self.hm[key])
            return self.hm[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node = self.hm[key]
            node.value = value
            self.removeNode(node) #forgot to remove
            self.addToHead(node)
        else:
            self.hm[key] = Node(key,value)
            self.addToHead(self.hm[key])
            if len(self.hm) > self.capacity:
                lastNode = self.tail.prev 
                key = lastNode.key
                self.removeNode(lastNode) #not remove from tail
                del self.hm[key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)