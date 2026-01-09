#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int prev1 = cost[0], prev2 = cost[1];
        for (int i = 2; i < cost.size(); i++){
            int temp = prev2;
            prev2 = min(cost[i] + prev1, cost[i] + prev2);
            
            prev1 = temp;
        }

        return min(prev1,prev2);
    }
};

int main(){
    Solution s;
    vector<int> cost = {10,15,20,5,5,100};
    int ans = s.minCostClimbingStairs(cost);
    cout << ans << endl;
}