class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            prod = 1
            temp = []
            for j in range(len(nums)):
                if i != j:
                    temp.append(nums[j])
            
            
            for k in temp:
                prod = prod * k
            
            res.append(prod)
            

            
        return res

        