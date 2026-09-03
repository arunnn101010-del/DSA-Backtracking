# Promblem - combination sum 
# approach - backtracking 
# Time and space complexity - 0(n * n ) & 0(n) 
# Leetcode and diffculty level - 39 & medium 
class Solution {
public:
    void solve(vector<int>& candidates, int i, int target,
               vector<int>& curr, vector<vector<int>>& ans) {

        if(target == 0) {
            ans.push_back(curr);
            return;
        }

        if(i == candidates.size() || target < 0)
            return;

        curr.push_back(candidates[i]);

        solve(candidates, i, target - candidates[i], curr, ans);

        curr.pop_back();

        solve(candidates, i + 1, target, curr, ans);
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {

        vector<vector<int>> ans;
        vector<int> curr;

        solve(candidates, 0, target, curr, ans);

        return ans;
    }
};
