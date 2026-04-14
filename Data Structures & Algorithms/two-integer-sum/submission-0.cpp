class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
              for (int i = 0; i < n; i++ ) { // Using for loops to search all possible pairs for adding target
          for (int j = i + 1; j <n; j++) {
              if (nums[i] + nums[j] == target) {
                  return {i,j};
              }; // adding two indices will return target
              }

          }
          return {};



       

        
    }
};
