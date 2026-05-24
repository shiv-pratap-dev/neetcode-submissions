class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            if i == len(numbers) - 1:
                continue
            for j in range(1, len(numbers)):
                if i<j and numbers[i] != numbers[j]:
                    if numbers[i] + numbers[j] == target:
                        return list([i+1,j+1])

        