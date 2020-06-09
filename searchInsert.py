class Solution:
    """Purpose: Returns the index if target is found.
    If not, returns the index where it would be if it were inserted in order.
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(nums == [] or nums == None):
            return
        if(target <= nums[0]):
            return 0
        if(target > nums[-1]):
            return len(nums)

        
        for i in range(len(nums)-1):
            if(nums[i] < target and nums[i+1] >= target):  
                return i+1
            
                