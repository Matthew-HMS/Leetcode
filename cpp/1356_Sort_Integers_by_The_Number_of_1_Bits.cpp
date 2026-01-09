#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    vector<int> sortByBits(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        vector<int> counter_all;
        int temp;

        // find how many 1
        for (int i=0; i<arr.size(); i++){
            int counter = 0, n;
            temp = arr[i];
            while (arr[i] > 0){
                n = arr[i] % 2;
                arr[i] /= 2;
                if (n == 1){
                    counter++;
                }
            }

            arr[i] = temp;
            counter_all.push_back(counter);
        }

        // reorder by 1
        for (int j = 0; j < counter_all.size(); j++){
            for (int i = 1; i < counter_all.size(); i++){
                if (counter_all[i-1] > counter_all[i]){
                    temp = counter_all[i-1];
                    counter_all[i-1] = counter_all[i];
                    counter_all[i] = temp;

                    temp = arr[i-1];
                    arr[i-1] = arr[i];
                    arr[i] = temp;
                }
            }
        }


        return arr;
    }
};

int main(){
    Solution s;
    vector<int> arr = {0,1,2,3,4,5,6,7,8};
    vector<int> ans = s.sortByBits(arr);
    for (int e : ans){
        cout << e << endl;
    }
    
}