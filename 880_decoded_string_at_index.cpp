#include<iostream>
using namespace std;

class Solution {
public:
    string decodeAtIndex(string s, int k) {

        string output = "";
        for (char c : s){
            if(isdigit(c)){
                int repeat = c - '0';
                string repeat_out = "";
                for (int j=0; j<repeat; j++){
                    repeat_out += output;
                    if (repeat_out.length() > k){
                        break;
                    }
                }
                output = repeat_out;
            }
            else{
                output += c;
            }
            if (output.length() > k){
                break;
            }
        }

        return output.substr(k-1, 1);
    }
};

int main(){
    Solution s;
    string str;
    int k;

    str = "y959q969u3hb22odq595";
    k = 222280369;

    string result = s.decodeAtIndex(str,k);
    // print the result
    cout << result << endl;

    return 0;
}