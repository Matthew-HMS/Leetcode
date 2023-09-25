#include<iostream>
using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0, j = 0;
        // for (int i=0; i<s.length(); i++){
        //     for (int j=start; j<t.length(); j++){
        //         if (s[i] == t[j]){
        //             count++;
        //             start = j+1;
        //             break;
        //         }

        //     }
        // }

        while (i < s.length() && j < t.length()){
            if (s[i] == t[j]){
                i++;
            }
            j++;
        }

        return i == s.length();
    }
};


int main(){
    Solution s;
    string str,t;

    str = "ab";
    t = "baab";
    bool result = s.isSubsequence(str,t);
    // print the result
    cout << result << endl;

    return 0;
}