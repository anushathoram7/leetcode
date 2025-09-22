class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node1, node2):
            if node1:
                if node1 == target:
                    return node2
                left = dfs(node1.left, node2.left)
                if left:
                    return left
                return dfs(node1.right, node2.right)
        
        return dfs(original, cloned)
