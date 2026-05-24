class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> res;
        for(int i =0; i< numbers.size(); i++){
         
         for(int j = 1; j< numbers.size(); j++){
             if(i < j && (numbers[i] != numbers[j])){
                 if(numbers[i]+ numbers[j] == target){
                    return res = {i+1, j+1};
                 }
             }
         }
     }
    }
};
