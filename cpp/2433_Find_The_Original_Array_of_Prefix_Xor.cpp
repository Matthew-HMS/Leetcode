#include<iostream>
#include<bitset>
#include<vector>
using namespace std;


class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        int num = 0, result;
        vector<int> ans;

        for (int i = 0; i < pref.size(); i++){
            result = num ^ pref[i];
            ans.push_back(result);
            num = pref[i];
        }


        return ans;
    }
};

int main(){
    Solution s;
    vector<int> arr = {5,2,0,3,1};
    vector<int> ans = s.findArray(arr);
    for (int e : ans){
        cout << e << endl;
    }
    
}