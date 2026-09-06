# Promblem - palindrome partitioning 
# Approach - backtracking 
# Time and space complexity - 0(n * 2 ^ n) & 0(n) 
# Leetcode and diffculty level - 131 & medium 
class Solution {
public:

    bool isPalindrome(string& s, int left, int right) {

        while(left < right) {

            if(s[left] != s[right])
                return false;

            left++;
            right--;
        }

        return true;
    }

    void solve(string& s, int start,
               vector<string>& curr,
               vector<vector<string>>& ans) {

        if(start == s.size()) {
            ans.push_back(curr);
            return;
        }

        for(int i = start; i < s.size(); i++) {

            if(!isPalindrome(s, start, i))
                continue;

            curr.push_back(s.substr(start, i - start + 1));

            solve(s, i + 1, curr, ans);

            curr.pop_back();
        }
    }

    vector<vector<string>> partition(string s) {

        vector<vector<string>> ans;
        vector<string> curr;

        solve(s, 0, curr, ans);

        return ans;
    }
};
