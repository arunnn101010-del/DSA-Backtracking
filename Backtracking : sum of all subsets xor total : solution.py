# promblem - sum of all subsets of xor total
# Approach - backtracking + bit manipulation 
# Time and space complexity - 0(2^n) & 0(n) 
# Leetcode and diffculty level - 1863 & easy 
class Solution {
public:
    int ans = 0;

    void solve(vector<int>& nums, int i, int xr) {
        if(i == nums.size()) {
            ans += xr;
            return ;
        }

        solve(nums, i+1, xr ^ nums[i]);
        solve(nums, i+1, xr);
    }
    int subsetXORSum(vector<int>& nums) {
        solve(nums, 0, 0);
        return ans;
    }
};
