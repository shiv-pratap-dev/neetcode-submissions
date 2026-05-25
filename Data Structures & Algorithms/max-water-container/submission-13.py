class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0


    # this operates in o(n2) time 
        # for i in range(len(heights)):
        #     j = len(heights)-1

        #     while i < j:
        #         new_min = min(heights[i], heights[j])
        #         area = new_min * (j-i)
        #         max_area = max(max_area, area)

        #         j-=1

        l = 0
        r = len(heights)-1

        while l < r:
            new_min = min(heights[l], heights[r])
            max_area = max(max_area, (new_min * (r-l)))

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

            
        
        return max_area
        