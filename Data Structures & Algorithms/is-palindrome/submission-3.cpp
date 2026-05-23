class Solution {
public:
    bool isPalindrome(string s) {
    string rev = "";
    string revv = "";
    
    for(int i =0; i < s.length(); i++){
        if((isalnum(s[i]))){
            rev +=tolower(s[i]);
        }
    }
    
    for(int i = rev.length() -1; i>=0; i--){
        revv+= rev[i];
    } 
    
    
    if(revv==rev){
        return true;
    }
    else{
        return false;
    }

 }
};
