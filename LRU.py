class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache:
    
    def __init__(self, capacity: int):
        self.hm = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        
    def removeNode(self, curr):
        curr.next.prev = curr.prev 
        curr.prev.next = curr.next 
        
    def addToHead(self, node):
        node.next = self.head.next 
        node.next.prev = node
        self.head.next = node
        node.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1
        
        node = self.hm[key]
        self.removeNode(node)
        self.addToHead(node)
        return node.val #node

    def put(self, key: int, value: int) -> None:
        #if it exists, update and update LL
        if key in self.hm:
            node = self.hm[key]
            node.val = value
            
            self.removeNode(node)
            self.addToHead(node)
            
        #doesn't exist. SO make the node, add it to the linked list.
        else:
            newNode = Node(key,value)
            if self.capacity == len(self.hm):
                tailPrev = self.tail.prev
                self.removeNode(tailPrev)
                del self.hm[tailPrev.key]
            self.addToHead(newNode)
            self.hm[key] = newNode

        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)