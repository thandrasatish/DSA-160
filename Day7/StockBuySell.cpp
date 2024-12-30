#include<bits/stdc++.h>
using namespace std;

int StockBuySell(vector<int> prices, int n){

    int res=0;
    int minsofar=prices[0];
    for(int i=1;i<n;i++){
        minsofar = min(minsofar,prices[i]);
        res=max(res,prices[i]-minsofar);
    }

    return res;


}

int main(){
    vector<int> prices = {7,10,1,3,6,9,2};
    int n= prices.size();

    int r = StockBuySell(prices,n);
    cout<<"result:"<<r<<endl;
};