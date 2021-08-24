class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        x = []
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        for i in range(len(horizontalCuts)+1):
            if i == 0:
                x.append(horizontalCuts[i])
            elif i == len(horizontalCuts):
                x.append(h-horizontalCuts[i-1])
            else:
                x.append(horizontalCuts[i] - horizontalCuts[i-1])
        x = max(x)
        y = []
        for i in range(len(verticalCuts)+1):
            if i == 0:
                y.append(verticalCuts[i])
            elif i == len(verticalCuts):
                y.append(w-verticalCuts[i-1])
            else:
                y.append(verticalCuts[i] - verticalCuts[i-1])
        mx = float('-inf')
        y = max(y)
        # for i in y:
        #     for j in x:
        #         mx = max(mx, i*j)
        mx = x*y
        return ((mx)%((10**9)+7))