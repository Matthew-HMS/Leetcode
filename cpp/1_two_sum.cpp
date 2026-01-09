#include<iostream>
#include<vector>
using namespace std;


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        int n = nums.size();
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                if (nums[i] + nums[j] == target) return {i,j};
            }
        }
        return {}; // add this line to return an empty vector if no solution is found
    }
};


int main(){
    Solution s;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = s.twoSum(nums, target);
    // print the result
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    return 0;
}