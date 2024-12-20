// Link URL:- https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/move-all-zeroes-to-end-of-array0751


#include <bits/stdc++.h>
using namespace std;

int secondLargest(vector<int> &nums){

    int n = nums.size();
    int max_ele = *max_element(nums.begin(),nums.end());

    int sec_max=-1;
    for(int i=0;i<n;i++){
        if(nums[i]<max_ele){
            sec_max=max(nums[i],sec_max);
        }
    }

    return sec_max;

}

int main(){

    int t;
    cin>>t;
    vector<int> nums;
    while(t--){
        int n;
        cin>>n;
        nums.push_back(n);

    }

    cout<<secondLargest(nums)<<endl;

};
