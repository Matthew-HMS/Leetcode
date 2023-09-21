#include<iostream>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0) return false;
        string s = to_string(x);
        string output = "";

        do {
            int num = x%10;
            output += to_string(num);
            x /= 10;
        } while (x > 0);

        if (output == s) {
            return true;
        }
        else return false;

    }
};


int main(){
    Solution s;
    int x = 0;
    bool result = s.isPalindrome(x);
    // print the result
    cout << result << endl;

    return 0;
}