#include<stdio.h>
#include<iostream>
#include<string>
#include<typeinfo>
#include<map>

using namespace std;


bool evenCharacters(string x){
	if (x.size()%2 == 0){
		return true;
	}
	return false;

}


bool countVowels(string x){
	map<char, int> vowels;
		vowels['a'] = 1;
		vowels['e'] = 1;
		vowels['i'] = 3;
		vowels['o'] = 1;
		vowels['u'] = 1;

	map<char, int>::iterator it = vowels.begin();
	for(; it!=vowels.end(); it++){
		cout << it->first << "," << it->second << endl;
	}
}
map<char, int> countNumRepeatLetters(string s){
	map<char, int> abc;
	map<char, int>::iterator it;
	for(int i=0; i<s.size(); i++){
		it = abc.find(s[i]);
		if (it != abc.end()){
			int value = it->second + 1;
			abc[s[i]] = value;
		}
		else{
			abc[s[i]] = 1;
		}
		it = abc.find(s[i]);
		cout<<"first: " << it->first << ", second: " << it->second << endl;
	}
	return abc;
	
}

int main(void){

string s = "wowzaa";

cout << evenCharacters(s) << endl;
countNumRepeatLetters(s);
countVowels(s);

return 0;
}