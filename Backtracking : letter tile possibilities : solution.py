# promblem - letter tile possbilities 
# Approach - backtracking 
# Time and space complexity - 0(n) & 0(n) 
# Diffculty level and leetcode - easy & 1079 
class Solution {
public:
    int solve(vector<int>& count) {
        int ans = 0;

        for(int i = 0; i < 26; i++) {
            if(count[i] == 0) 
                continue;
            count[i]--;
            ans++;

            ans += solve(count);

            count[i]++;
        }
        return ans;
    }
    int numTilePossibilities(string tiles) {
        vector<int> count(26);

        for(char c : tiles) {
            count[c - 'A']++;
        }
        return solve(count);
    }
};
