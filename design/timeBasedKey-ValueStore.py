"""
    So the plan is to create a hashmap that stores the key: and the value would be a dictionary as well.
    In the nested dictionary.. it will hold the value and the timestamps.
    When getting from hashmap.. we will check if it exists. In this hashmap,
    check for timestamp and if it is in the nested dictionary return it.. else decrease timestamp until we see a valid one
"""

class TimeMap:

    def __init__(self):
        self.hm = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hm:
            self.hm[key] = {timestamp:value}
        else:
            #go into the dictionary
            hm = self.hm[key]
            hm[timestamp] = value
            

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm:
            return ""
        hm = self.hm[key]
        while timestamp > 0:
            if timestamp in hm:
                return hm[timestamp]
            timestamp -= 1
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)