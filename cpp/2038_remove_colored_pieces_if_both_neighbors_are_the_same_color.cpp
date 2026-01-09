#include<iostream>
using namespace std;

class Solution {
public:
    bool winnerOfGame(string colors) {
        int counter_a = 0, counter_b = 0;

        for (int i=1; i<colors.length()-1; i++){
            if (colors[i-1] == colors[i] && colors[i] == colors[i+1]){
                if (colors[i] == 'A'){
                    counter_a++;
                }
                else if (colors[i] == 'B'){
                    counter_b++;
                }
            }
        }

        if (counter_a == counter_b || counter_a < counter_b) return false;
        else return true;

    }
};

int main(){
    Solution s;
    string color = "AAABBA";
    bool ans = s.winnerOfGame(color);

    cout << ans << endl;
}