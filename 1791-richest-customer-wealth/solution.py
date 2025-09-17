class Solution:
    def maximumWealth(self, accounts):
        maxsum = 0
        m = len(accounts)
        for i in range(m):
            rowsum = sum(accounts[i])
            if rowsum > maxsum:
                maxsum = rowsum
        return maxsum
        
