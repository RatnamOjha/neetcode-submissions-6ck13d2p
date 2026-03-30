class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        unordered_map<char,int> letterS;
        unordered_map<char,int> letterT;
         
        for(char c : s){
            letterS[c]++;
        } 

        for(char c : t){
            letterT[c]++;
        }

        return letterS == letterT;
    }
};
