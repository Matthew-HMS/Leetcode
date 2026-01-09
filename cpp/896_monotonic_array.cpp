#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        vector<int> nums_2 = {nums[0]};
        for (int i=1; i<nums.size(); i++){
            if (nums[i-1] != nums[i]){
                nums_2.push_back(nums[i]);
            }
        }

        for (int i=1; i<nums_2.size()-1; i++){
            if (nums_2[i-1] < nums_2[i] && nums_2[i] > nums_2[i+1]) return false;
            if (nums_2[i-1] > nums_2[i] && nums_2[i] < nums_2[i+1]) return false;
        }

        return true;
    }
};


int main(){
    Solution s;
    vector<int> nums = {1,3,2};
    bool ans = s.isMonotonic(nums);

    cout << ans;
}