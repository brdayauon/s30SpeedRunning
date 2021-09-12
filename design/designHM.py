class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = math.ceil(math.sqrt(1000000))
        #print(self.size)
        self.arr = [[False for i in range(self.size+1)] for j in range(self.size+1)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash1 = key % self.size
        hash2 = key // self.size
        if self.arr[hash1][hash2] == False:
            self.arr[hash1][hash2] = value
        
        self.arr[hash1][hash2] = value
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash1 = key % self.size
        hash2 = key // self.size
        if self.arr[hash1][hash2] is not False:
            return self.arr[hash1][hash2]
            
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash1 = key % self.size
        hash2 = key // self.size
        
        if self.arr[hash1][hash2] is not False:
            self.arr[hash1][hash2] = False


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)