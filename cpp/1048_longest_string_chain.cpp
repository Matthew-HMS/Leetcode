#include<iostream>
#include<vector>
#include<algorithm>
#include<unordered_map>

using namespace std;

class Solution {
public:
    int longestStrChain(vector<string>& words) {
        unordered_map<string, int> dp;
        int res = 0;
        sort(words.begin(), words.end(), [](const string& a, const string& b){
            return a.length() < b.length();
        });
        for (string& word : words){
            int len = 1;
            for (int i=0; i<word.length(); i++){
                // prev.erase(i,1);
                string prev = word.substr(0,i) + word.substr(i+1);
                len = max(dp[prev]+1, len);
            }
            dp[word] = len;
            res = max(res, len);
        }

        return res;

    }
};


int main(){
    Solution s;

    vector<string> words = {"a","b","ba","bca","bda","bdca"};
    int result = s.longestStrChain(words);
    // print the result
    cout << result << endl;

    return 0;
}
