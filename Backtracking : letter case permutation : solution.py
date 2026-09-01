# Promblem - letter case permutation 
# Approach - backtracking 
# Time and space complexity - 0(2^n * 2) & 0(n) 
# Leetcode and diffculty level - 784 & easy 
class Solution {
public:
    void solve(string& s, int i, vector<string>& ans) {

        if(i == s.size()) {
            ans.push_back(s);
            return;
        }

        if(isalpha(s[i])) {

            s[i] = tolower(s[i]);
            solve(s, i + 1, ans);

            s[i] = toupper(s[i]);
            solve(s, i + 1, ans);
        }
        else {
            solve(s, i + 1, ans);
        }
    }

    vector<string> letterCasePermutation(string s) {

        vector<string> ans;
        solve(s, 0, ans);

        return ans;
    }
};
