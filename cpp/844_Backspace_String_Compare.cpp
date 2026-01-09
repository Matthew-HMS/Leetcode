#include<iostream>
#include<vector>
using namespace std;


class Solution {
public:
    bool backspaceCompare(string s, string t) {
        string s_cp = "", t_cp = "";
        for (char c : s){
            if (c == '#' && s_cp != ""){
                s_cp.erase(s_cp.length()-1);
            }
            else if(c != '#'){
                s_cp += c;
            }
        }

        for (char c : t){
            if (c == '#' && t_cp != ""){
                t_cp.erase(t_cp.length()-1);
            }
            else if(c != '#') {
                t_cp += c;
            }
        }

        return (s_cp == t_cp);
    }
};

int main(){
    Solution s;
    string str = "y#fo##f"; 
    string t = "y#f#o##f";
    bool ans = s.backspaceCompare(str,t);

    cout << ans;
}