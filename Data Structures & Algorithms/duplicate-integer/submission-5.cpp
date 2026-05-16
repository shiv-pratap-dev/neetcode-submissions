class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        vector<int> checkArray;

        for(int i =0; i< nums.size(); i++){
            for(int j = 0; j< checkArray.size(); j++){
                if(nums[i] == checkArray[j]){
                    return true;
                }
               
            }
            checkArray.push_back(nums[i]);
        }

        return false;
    }
};