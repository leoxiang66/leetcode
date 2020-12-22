#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
class Solution {
public:
    int firstUniqChar(string s1234556) {
         char ret= rec(s1234556);
         if(ret !='.') return s1234556.find(ret);
         return  -1;

    }

    char rec(string s1){
        
        if (s1 == "" ){
            return '.';
        } else if (s1.size()==1) return s1[0];

        char peek = s1[0];
        string rest =  s1.substr(1);

        if (rest.find(peek)==string::npos){
            return peek;
        }
        else   {
           rest.erase(std::remove(rest.begin(), rest.end(), peek), rest.end());
            return rec(rest);
        }
    }
};

