class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        newBed = [0] + flowerbed + [0]
        length = len(flowerbed)
        for i in range(1, length+1):
            if newBed[i] == 0 and newBed[i-1] == 0 and newBed[i+1] == 0:
                newBed[i] = 1
                n -= 1
        
        if n > 0:
            return False
        
        return True