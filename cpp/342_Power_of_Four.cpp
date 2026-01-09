#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    bool isPowerOfFour(int n) {
        double temp = n;
        while (temp >= 4){
            temp /= 4;
        }
        if (temp == 1) return true;
        else return false;
    }
};

int main(){
    Solution s;
    int num = 1;
    bool ans = s.isPowerOfFour(num);
    cout << ans << endl;
    
}