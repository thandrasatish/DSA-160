#include<bits/stdc++.h>

using namespace std;

int secondlargest(vector<int> &arr, int n){
    
    int max_ele = *max_element(arr.begin(),arr.end());
    int sec_max=-1,i=0;
    
    for(i=0;i<n;i++){
        if(arr[i]<max_ele){
            sec_max = max(sec_max,arr[i]);
        }
        
    }
    
    return sec_max;
    
}

int main(){
    
    int i,n,m,res;
    cin>>n;
    vector<int> nums;
    for(i=0;i<n;i++){
        cin>>m;
        nums.push_back(m);
    }
    
    res=secondlargest(nums,n);
    
    cout<<res<<endl;
    
    
    
    
}