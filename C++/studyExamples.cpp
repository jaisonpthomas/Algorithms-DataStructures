#include <map>
#include <iostream>

class RomanNumerals()
{
    int romanNumerals()
    {
        //std::map<int, std::string, std::greater<int>> romans = {
        std::map<int, std::string> const romans =
        {
        {1, "I"},
        {4, "IV"},
        {5, "V"},
        {9, "IX"},
        {10, "X"},
        {40, "XL"},
        {50, "L"},
        {90, "XC"},
        {100, "C"},
        {400, "CD"},
        {500, "D"},
        {900, "CM"},
        {1000, "M"}
        };

        int number = 99;

        std::string res;

        for(auto x: romans)
        {
            std::cout << "Left Val: " << x.first << "\t\t";
            std::cout << "Right Val: " << x.second << '\n';
        }
    }
}

class findTheDifference
{
    char findTheDifference(std::string s, std::string t)
    {
        std::unordered_map<char, int> myMap;
        std::string combinedString = s+t;
        for (auto ch : combinedString)
            ++myMap[ch];

        for (auto iter: myMap) {
            if(iter.second % 2 != 0)
                return iter.first;
        
    }
    /*
    int main()
    {
        char diff = findTheDifference("abc", "caab");
        std::cout << diff;
    }
    */
}

class Solution
{
public:
    string toGoatLatin(string S)
    {
        //Intializers
        string word, trailingAs;
        stringstream iss(S), oss;
        
        //hashSet
        string vowelString = "aeiouAEIOU";
        unordered_set<char> vowelSet;
        for (int i=0; i<vowelString.length(); i++)
            vowelSet.insert(vowelString[i]);
        
        while(iss >> word)
        {
            trailingAs.push_back('a');
            auto iter = vowelSet.find(word[0]);
            if (iter != vowelSet.end())
                oss << " " << word << "ma" << trailingAs;
            else
                oss << " " << word.substr(1) << word[0] << "ma" << trailingAs;
        }
        return oss.str().substr(1);
    }
};

class reverseStringComponents
{
    string reverseStr(string s, int k)
    {
        for (int i = 0; i < s.size(); i += 2 * k)
            reverse(&s[i], &s[min(int(s.size()), i + k)]);
                           //up to the end, or i+k, whichever comes first
        return s;
    }
    /*
    int main()
    {
        string s = "abcdefg";
        int k = 2;
        string output = reverseStr(s, k);
        cout << output;
    }
    */
    /*
    def reverseStr(s, k):
    a = list(s)
    for i in range(0, len(a), 2*k):
        a[i:i+k] = reversed(a[i:i+k])
    return "".join(a)
    */
}

/*
def stringCompression(chars):
    anchor = write = 0
    for read, c in enumerate(chars):
        if read + 1 == len(chars) or chars[read + 1] != c:
            chars[write] = chars[anchor]
            write += 1
            if read > anchor:
                for digit in str(read - anchor + 1):
                    chars[write] = digit
                    write += 1
            anchor = read + 1
    return write

alpha = ["a","a","a","a","b","b","c","c","c"]
alphaEnd = stringCompression(alpha)
alpha = alpha[:alphaEnd]
*/