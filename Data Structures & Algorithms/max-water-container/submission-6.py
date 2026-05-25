class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for i in range(len(heights)):
            j = len(heights)-1

            while i < j:
                new_min = min(heights[i], heights[j])
                area = new_min * (j-i)
                max_area = max(max_area, area)

                j-=1
            
        
        return max_area
        