// Stock Buy and Sell – Max one Transaction Allowed
// Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

// Note: Stock must be bought before being sold.

// Examples:

// Input: prices[] = [7, 10, 1, 3, 6, 9, 2]
// Output: 8
// Explanation: You can buy the stock on day 2 at price = 1 and sell it on day 5 at price = 9. Hence, the profit is 8.

#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int maximumProfit(vector<int> &prices) {
        int min_num = prices[0];  // Initialize minimum price to the first element
        int max_num = INT_MIN;   // Initialize maximum profit to the smallest possible value
        int n = prices.size();   // Get the size of the prices array
        
        for (int i = 0; i < n; i++) {
            // Update the minimum price encountered so far
            min_num = min(min_num, prices[i]);
            // Calculate the profit by selling at the current price
            int profit = prices[i] - min_num;
            // Update the maximum profit if the current profit is higher
            max_num = max(max_num, profit);
        }
        
        return max_num; // Return the maximum profit
    }
};

int main() {
    Solution solution;
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    
    int result = solution.maximumProfit(prices);
    cout << "Maximum Profit: " << result << endl;
    
    return 0;
}
