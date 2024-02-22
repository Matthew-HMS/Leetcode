#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int i = 0, j = 0, counter = 0;
        while (i < nums.size()-1){
            if (nums[i] == nums[j] && i < j){
                counter++;
            }

            if (j == nums.size()-1) {
                i++;
                j = i + 1;
            }
            else j++;
        }

        return counter;
    }
};


int main(){
    Solution s;
    vector<int> input = {1,2,3,1,1,3};
    int ans = s.numIdenticalPairs(input);

    cout << ans << endl;
}