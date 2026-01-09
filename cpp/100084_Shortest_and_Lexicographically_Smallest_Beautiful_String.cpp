#include<iostream>
#include<vector>
#include<bitset>
using namespace std;

class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        int counter = 0;
        vector<int> lens = {};
        string output = "";

        for (int i=0; i<s.length(); i++){
            for (int j=i; j<s.length(); j++){
                if (s[j] == '1'){
                    counter++;
                }
                if (counter == k){
                    lens.push_back(j-i+1);
                    break;
                }
            }
            counter = 0;
        }

        if (lens.size() == 0) return output;

        vector<int> same = {};
        int min_len = lens[0], index = 0;
        for (int i=0; i<lens.size(); i++){
            if (lens[i] < min_len){
                min_len = lens[i];
                index = i;
                same = {i};
            }
            if (lens[i] == min_len){
                same.push_back(i);
            }
        }

        vector<string> nums = {};
        for (int j=0; j<same.size(); j++){
            for (int i=same[j]; i< same[j]+min_len; i++){
                output += s[i];
            }
            nums.push_back(output);
            output = "";
        }

        string ans = nums[0];
        bitset<32> binary(nums[0]);
        int min_nums = binary.to_ulong();
        for (int i=0; i<nums.size(); i++){
            bitset<32> binary(nums[i]);
            int num = binary.to_ulong();
            if (num < min_nums){
                min_nums = num;
                ans = nums[i];
            }
        }

        return ans;

    }
};

int main(){
    Solution s;
    string str = "110101000010110101";
    int k = 3;
    string ans = s.shortestBeautifulSubstring(str,k);
    cout << ans << endl;
}