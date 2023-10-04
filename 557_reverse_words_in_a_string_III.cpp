#include<iostream>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        string output = "";
        int end = s.length()-1;
        int start = 0;
        while (start < s.length()){
            for (int i=start; i<s.length(); i++){
                if (s[i] == ' '){
                    end = i-1;
                    break;
                }
            }

            for (int j=end; j>=start; j--){
                output += s[j];
            }

            if (end != s.length()-1) output += " ";
            start = end+2;
            end = s.length()-1;
        }

        return output;
    }
};

int main(){
    Solution s;
    string str = "God Ding";
    string ans = s.reverseWords(str);

    cout << ans << endl;
}