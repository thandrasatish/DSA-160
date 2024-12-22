// Reverse an Array:- https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/reverse-an-array



#include<bits/stdc++.h>
using namespace std;

void reverseArray(vector<int> &arr){

    int n = arr.size();
    int n1 = n/2;
    int i=0;
    while(i<n1){
        swap(arr[i],arr[n-i-1]);
        i++;
    }

}

int main(){
    int n;
    cin>>n;
    vector<int> arr;
    int new_num;
    while(n--){
        cin>>new_num;
        arr.push_back(new_num);
    }

    reverseArray(arr);

    for(auto ar:arr){
        cout<<ar<<" "<<endl;
    }

}
