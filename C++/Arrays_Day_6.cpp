// Stock Buy and Sell - Multiple Transaction Allowed
// The cost of stock on each day is given in an array price[]. Each day you may decide to either buy or sell the stock at price[i], you can even buy and sell the stock on the same day. Find the maximum profit that you can get.

// Note: A stock can only be sold if it has been bought previously and multiple stocks cannot be held on any given day.

// Examples:

// Input: prices[] = [100, 180, 260, 310, 40, 535, 695]
// Output: 865
// Explanation: Buy the stock on day 0 and sell it on day 3 => 310 – 100 = 210. Buy the stock on day 4 and sell it on day 6 => 695 – 40 = 655. Maximum Profit = 210 + 655 = 865.

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maximumProfit(vector<int>& prices) {
        int n = prices.size();
        int profit = 0;
        
        // Traverse through all days, and sum up all the profit we can gain
        for (int i = 1; i < n; i++) {
            if (prices[i] > prices[i - 1]) {
                profit += (prices[i] - prices[i - 1]);  // Buy on the previous day and sell on the current day
            }
        }
        
        return profit;  // Return the total profit
    }
};

int main() {
    // Create an instance of Solution
    Solution sol;
    
    // Example usage
    vector<int> prices = {1, 7, 5, 3, 6, 4, 8};
    
    // Call the maximumProfit function and print the result
    int result = sol.maximumProfit(prices);
    cout << "Maximum profit: " << result << endl;
    
    return 0;
}
