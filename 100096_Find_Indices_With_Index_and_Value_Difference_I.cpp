#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<int> findIndices(vector<int>& nums, int indexDifference, int valueDifference) {
        vector<int> ans = {-1,-1};
        for (int i=0; i<nums.size(); i++){
            for (int j=i+indexDifference; j<nums.size(); j++){
                if (abs(nums[j] - nums[i]) >= valueDifference){
                    ans = {};
                    ans.push_back(i);
                    ans.push_back(j);
                    return ans;
                }
            }
        }
        return ans;
    }
};

int main(){
    Solution s;
    vector<int> nums = {1,2,3};
    int indexdiff = 2;
    int valuediff = 4;
    vector<int> ans = s.findIndices(nums, indexdiff, valuediff);
    for (int value : ans){
        cout << value << endl;
    }
}