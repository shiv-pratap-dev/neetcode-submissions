class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # groups = {}

        # for s in strs:
        #     key = "".join(sorted(s))

        #     if key not in groups:
        #         groups[key] = []
            
        #     groups[key].append(s)

        # return list(groups.values())

        sortedstr = []
        result = []

        visited = set()

        for i in strs:
            sortedstr.append("".join(sorted(i)))
            

        for i in range(len(strs)):
            if i in visited:
                continue
            
            new_list = [strs[i]]
            for j in range(i+1, len(strs)):
                if sortedstr[i] == sortedstr[j]:
                    new_list.append(strs[j])
                    visited.add(j)
            

            result.append(new_list)

        return result
        
        