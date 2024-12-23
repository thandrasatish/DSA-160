#include<bits/stdc++.h>
using namespace std;
void reverseAnArray(int d, int n, vector<int>& arr){
    
    d=d%n;

    reverse(arr.begin(),arr.begin()+d);
    reverse(arr.begin()+d,arr.end());
    reverse(arr.begin(),arr.end());
    cout<<"In the Function"<<endl;
    for(auto &ar:arr){
        cout<<ar<<" ";
    }

};

int main(){
    int n;
    cin>>n;
    int d;
    cin>>d;
    vector<int> arr;
    int n1;
    for(int i=0;i<n;i++){
        cin>>n1;
        arr.push_back(n1);
    }
    reverseAnArray(d,n,arr);
    cout<<"Outside the function"<<endl;
    for(auto &ar:arr){
        cout<<ar<<" ";
    }
}