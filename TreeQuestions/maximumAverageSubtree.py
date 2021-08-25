class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        """
        Go to the bottom of the tree and go up from the leaf (updating hashmap to help)
        """

        if not root:
            return 0
        mx = 0
        hm = {None:(0,0)} #node : (sum,count)
        stack = [root]

        while stack:
            curr = stack.pop()
            if curr:
                if curr.left in hm and curr.right in hm:
                    #get and update values
                    sumOfSubtree1, countOfSubTree1 = hm[curr.left]
                    sumOfSubtree2, countOfSubTree2 = hm[curr.right]

                    #update values
                    currSum = sumOfSubtree1 + sumOfSubtree2 + curr.val
                    currCount = countOfSubTree1 + countOfSubTree2 + 1
                    hm[curr] = (currSum,currCount)
                    mx = max(mx, currSum/currCount)
                     
                else:
                    stack.append(curr)
                    stack.append(curr.left)
                    stack.append(curr.right)
        return mx