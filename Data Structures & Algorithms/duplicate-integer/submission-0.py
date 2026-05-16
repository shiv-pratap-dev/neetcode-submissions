class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_arr= [];
        for i in range(len(nums)):
            if not (nums[i] in check_arr):
                check_arr.append(nums[i])
            else:
                return True
            
        return False
        