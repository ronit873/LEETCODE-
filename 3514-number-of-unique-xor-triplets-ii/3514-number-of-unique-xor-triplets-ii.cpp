class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        unordered_set<int> st(nums.begin(), nums.end());

        const int MAXX = 2048;
        vector<bool> two(MAXX, false);
        vector<bool> ans(MAXX, false);

        vector<int> vals(st.begin(), st.end());

        // All x ^ y
        for (int x : vals)
            for (int y : vals)
                two[x ^ y] = true;

        // (x ^ y) ^ z
        for (int v = 0; v < MAXX; v++) {
            if (!two[v]) continue;
            for (int z : vals)
                ans[v ^ z] = true;
        }

        return count(ans.begin(), ans.end(), true);
    }
};