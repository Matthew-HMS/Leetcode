#include<iostream>
#include<vector>
#include<cmath>
#include<iomanip>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int count = (nums1.size() + nums2.size())/2;
        cout<<"count:"<<count<<endl;
        int i=0;int j=0;
        double ans = 0;

        while(count>0){
            if(nums1[i]<nums2[j] || j==nums2.size()){
                ans = nums1[i];
                i+=1;
                count=count-1;
                cout<<"i:"<<i<<endl;
            }
            else if(nums1[i]>nums2[j] || i==nums1.size()){
                ans = nums2[i];
                j+=1;
                count=count-1;
                cout<<"j:"<<j<<endl;
            }
            cout<<"!"<<count<<endl;
        }
            
        double ans_i = (nums1[i]+nums2[j])/2;

        cout<<"25"<<endl;
        if(count==0){
            cout<<"30"<<endl;
            return ans_i;   
        }
        // else if(count<0){
        //     return ans;
        //     cout<<"34"<<endl;
        // }

        cout<<ans<<""<<i<<""<<j;
        return 1.1;
        
    }
};

int main(){
    Solution s;
    vector<int> num1 = {1,3};
    vector<int> num2 = {2};
    double ans = s.findMedianSortedArrays(num1, num2);
    cout << setprecision(5) << fixed << ans << endl;
    
}