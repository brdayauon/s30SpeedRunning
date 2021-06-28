# We will be doing both the approaches recursive one and the iterative one. in this problem we will make sure 3 
# three things whther all the values on left are smaller than the root value and all the values on the right are greater than the current value.

# Recursive Solution:

# public class Solution {

# public boolean isValidBST(TreeNode root) {

#   return isValid(root, null, null);

# }

# public boolean isValid(TreeNode root, Integer min, Integer max) {

#   if(root == null) return true;

#   if(min != null && root.val <= min) return false;

#   if(max != null && root.val >= max) return false;

#   return isValid(root.left, min, root.val) && isValid(root.right, root.val, max);

# }}

# Iterative Solution:

# class Solution {

# public boolean isValidBST(TreeNode root) {

#       if (root == null) return true;

#       Stack <TreeNode> stack = new Stack<>();

#       TreeNode prev = null;

#       while(root != null || !stack.isEmpty()){

#           while(root != null){

#               stack.push(root);

#               root = root.left;

#           }

#           root = stack.pop();

#           if(prev != null && root.val <= prev.val) return false;

#           prev = root;

#           root = root.right;

#       }

#        return true;

#    }

# }





# python code:

# class Solution:

# 	def isValidBST1(self, root):

# 		return self.helper(root, None, None)

# 	def helper1(self, root, minVal, maxVal):

# 		if root == None:

# 			return True

# 		if minVal != None and root.val <= minVal:

# 			return False

# 		if maxVal != None and root.val >= maxVal:

# 			return False

# 		return self.helper(root.left, minVal, root.val) and self.helper(root.right, root.val, maxVal)

# 	def isValidBST2(self, root):

# 		if root == None:

# 			return True

# 		prev = None

# 		stack = []

# 		while(root != None or len(stack) > 0):

# 			while(root != None):

# 				stack.append(root)

# 				root = root.left

# 			root = stack.pop()

# 			if prev != None and root.val <= prev.val:

# 				return False

# 			prev = root

# 			root = root.right

# 		return True

# 	prev = None

# 	def isValidBST3(self, root):

# 		self.prev = None

# 		return self.helper(root)

# 	def helper3(self, root):

# 		if root == None:

# 			return True

# 		if not self.helper3(root.left):

# 			return False

# 		if self.prev != None and root.val <= self.prev.val:

# 			return False

# 		self.prev = root

# 		return self.helper3(root.right)