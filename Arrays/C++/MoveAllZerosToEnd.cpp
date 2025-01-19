#include<bits/stdc++.h>

using namespace std;

void MoveAllZerosToEnd(vector<int> &arr, int n){
    int i,j=0;
        
    for(i=0;i<n;i++){
        if(arr[i]!=0){
            swap(arr[i],arr[j]);
            j++;
        }
    }
    
}

int main(){
    
    int i,n,m,res;
    cin>>n;
    vector<int> nums;
    for(i=0;i<n;i++){
        cin>>m;
        nums.push_back(m);
    }
    
    MoveAllZerosToEnd(nums,n);
    
    for(i=0;i<n;i++){
        cout<<nums[i]<<endl;
    }
    
    
    
    
}