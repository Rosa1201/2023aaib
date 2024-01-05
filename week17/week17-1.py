class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 1
        table = [0]*N
        table[0] = 1
        for i in range(1,N):
            table[i] = 1
            for k in range(i):
                if nums[i]>nums[k] and table[k]+1>table[i]:
                    table[i] = table[k]+1
            if table[i] > ans: ans = table[i]
        return ans