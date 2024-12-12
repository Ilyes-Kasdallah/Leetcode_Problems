class Solution {
    bool isVow(char c) {
        return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
                c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
    }

public:
    string reverseVowels(string s) {
        int n = s.size();
        int left = 0, right = n - 1;
        while (left < right) {
            if (!isVow(s[left])) {
                left++;
            } else if (!isVow(s[right])) {
                right--;
            } else {
                swap(s[left], s[right]);
                left++;
                right--;
            }
        }
        
        return s;
    }
};
