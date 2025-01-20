#include<bits/stdc++.h>

using namespace std;

vector<int> reverseAnArray(vector<int> &arr, int &n){
    
    int m1=n/2;
    int j=0;
    while(m1!=0){
        swap(arr[j],arr[n-j]);
        m1--;
        j++;
    }
    
    return arr;
    
}

int main(){
    
    int i,n,m;
    vector<int> arr;
    for(i=0;i<n;i++){
        cin>>m;
        arr.push_back(m);
        
    }
    
    vector<int> new_arr;
    
    new_arr=reverseAnArray(arr,n);
    
    for(i=0;i<n;i++){
        cout<<new_arr[i]<<endl;
    }
}