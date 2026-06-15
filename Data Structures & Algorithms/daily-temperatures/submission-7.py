class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] *len(temperatures)
        temp =[]

        # for i in range(len(temperatures)):
        #     found = False
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j]> temperatures[i]:
        #             res.append(j-i)
        #             found = True
        #             break
            
        #     if not found:
        #         res.append(0)

        # return(res)

        for i in range(len(temperatures)):
            while temp and temperatures[temp[-1]] < temperatures[i]:
                j = temp.pop()
                res[j] = i-j

            temp.append(i)

        return res 
        
               