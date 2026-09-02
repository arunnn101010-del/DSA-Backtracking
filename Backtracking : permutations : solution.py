# Promblem - permutations 
# Approach - backtracking 
# Time and space complexity - 0(n * n!) & 0(n) 
# Leetcode and diffculty level - 46 & medium 
class Solution {
public:
    void solve(vector<int>& nums, vector<int>& curr,
               vector<vector<int>>& ans) {

        if(curr.size() == nums.size()) {
            ans.push_back(curr);
            return;
        }

        for(int i = 0; i < nums.size(); i++) {

            if(find(curr.begin(), curr.end(), nums[i]) != curr.end())
                continue;

            curr.push_back(nums[i]);

            solve(nums, curr, ans);

            curr.pop_back();
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {

        vector<vector<int>> ans;
        vector<int> curr;

        solve(nums, curr, ans);

        return ans;
    }
};
