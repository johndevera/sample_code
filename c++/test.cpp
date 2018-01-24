#include<stdio.h>
#include<iostream>
//#include<string>
#include<typeinfo>
#include<map>

using namespace std;

void printString(string x){
	cout << x << endl;
}

map<char, int> countNumRepeatLetters(string s){
	map<char, int> abc;
	map<char, int>::iterator it;

	for (int i=0; i<s.size(); i++){
		it = abc.find(s[i]);
		if (it != abc.end()){
			abc[s[i]] = it->second + 1;
		}
		else{
			abc[s[i]] = 1;
		}
		it = abc.find((s[i]));
		cout << "First: " << it->first << ", Second: " << it->second <<  endl;
	}
	return abc;
	
}

int main(void){
	
	string x = "shello";
	
	printString(x);
	int size = x.size();

	for (int i = 0; i < size/2; i++){
		char temp_begin = x[i];
		char temp_end = x[size-i-1];
		x[i] = temp_end;
		x[size-i-1] = temp_begin;
	}
	printString(x);
	countNumRepeatLetters(x);


	return 0;
}


// #include<stdio.h>
// #include<iostream>
// //#include<string>
// #include<typeinfo>
// #include<map>

// using namespace std;

// void printString(string x){
// 	cout << x << endl;
// }

// string reverseString(string x){
// 	int size = x.size();

// 	for (int i = 0; i < size/2; i++){
// 		char temp_begin = x[i];
// 		char temp_end = x[size-i-1];
// 		x[i] = temp_end;
// 		x[size-i-1] = temp_begin;
// 	}
// }

// int main(void){
	
// 	string x = "shello";
	
// 	//printString(x);
// 	string y = reverseString(x);
// 	//printString(y);




// 	return 0;



// }