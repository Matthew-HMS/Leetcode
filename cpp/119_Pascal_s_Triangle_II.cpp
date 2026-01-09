#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> new_row = {1};

        for (int i=0; i<rowIndex; i++){
            vector<int> temp = {1};
            for (int j=0; j<i; j++){
                temp.push_back(new_row[j] + new_row[j+1]);
            }
            temp.push_back(1);
            new_row = temp;
        }

        return new_row;
    }
};

int main(){
    Solution s;
    int row = 33;
    vector<int> ans = s.getRow(row);
    for (int i : ans){
        cout << i << endl;
    }
}