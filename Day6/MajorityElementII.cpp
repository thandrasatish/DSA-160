// Link:- https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/majority-vote
#include<bits/stdc++.h>
using namespace std;

vector<int> new_majority(int n, vector<int>& arr){
    
    map<int,int> freq;
    for(auto &ar:arr){
        freq[ar]++;
    }
    
    vector<int> new_arr;
    for(auto ne_ar:freq){
        if(ne_ar.second>(n/3)){
            new_arr.push_back(ne_ar.first);
        }
    }
    
    return new_arr;
    
    
    
}

int main(){
    int n;
    cin>>n;
    int i,m;
    vector<int> arr;
    for(i=0;i<n;i++){
        cin>>m;
        arr.push_back(m);
        
    }
    
    vector<int> new_freq_arr;
    
    new_freq_arr = new_majority(n,arr);
    
    for(auto n_f_a:new_freq_arr){
        cout<<n_f_a<<endl;
    }
    
    
    
}