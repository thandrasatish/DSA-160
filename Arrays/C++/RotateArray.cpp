#include<bits/stdc++.h>

using namespace std;

vector<int> rotateArray(vector<int> &arr, int &n, int &d){
    reverse(arr.begin(),arr.begin()+d);
    reverse(arr.begin()+d,arr.end());
    reverse(arr.begin(),arr.end());
    
    return arr;
    
}

int main(){
    
    int i,n,m,d;
    cin>>n;
    cin>>d;
    vector<int> arr;
    for(i=0;i<n;i++){
        cin>>m;
        arr.push_back(m);
        
    }
    
    vector<int> new_arr;
    
    new_arr=rotateArray(arr,n,d);
    
    for(i=0;i<n;i++){
        cout<<new_arr[i]<<endl;
    }
}