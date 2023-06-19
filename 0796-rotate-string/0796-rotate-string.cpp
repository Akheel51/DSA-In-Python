class Solution {
public:
    bool rotateString(string s, string goal) {
        if (s.length() != goal.length()) {
            return false;
        }

        int n = s.length();
        s += s;  // Concatenate s with itself

        for (int i = 0; i < n; i++) {
            if (s.substr(i, n) == goal) {
                return true;
            }
        }

        return false;
    }
};
