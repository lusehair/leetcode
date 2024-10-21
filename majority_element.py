class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        total = len(nums) 
        count = 1 
        nums.sort()
        for i in range(1, total) : 
            if nums[i] == nums[i-1] : 
                count += 1 
            else : 
                if count > total // 2 : 
                    return nums[i-1] 
                count = 1 
        if count > total // 2 : 
            return nums[-1]
