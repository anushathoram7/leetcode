from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1  # prefix sum = 0 occurs once
        
        curr_sum = 0
        result = 0
        
        for num in nums:
            curr_sum += num % 2  # add 1 if odd, 0 if even
            
            # check if there was a prefix with sum = curr_sum - k
            if curr_sum - k in count:
                result += count[curr_sum - k]
            
            # update count
            count[curr_sum] += 1
        
        return result
