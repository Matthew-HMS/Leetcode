#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        vector<int> ans;
        for (int& num : nums){
            if (num%2==0) ans.push_back(num);
        }
        for (int& num : nums){
            if (num%2!=0) ans.push_back(num);
        }

        return ans;
    }
};

int main(){
    vector<int> array = {0,1,2,3,4};
    Solution s;
    vector<int> ans = s.sortArrayByParity(array);
    for (int num : ans){
        cout << num << " ";
    }

}