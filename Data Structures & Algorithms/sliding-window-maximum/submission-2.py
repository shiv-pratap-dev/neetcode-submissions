class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = [0]*k
        max_list = []

        left = 0
        right = k-1

        if k==1:
            return nums

        while(left<right and right < len(nums)):
            window = nums[left:right+1]
            max_num = max(window)
            print(max_num)
            max_list.append(max_num)
            left+=1
            right+=1

        return(max_list)
        