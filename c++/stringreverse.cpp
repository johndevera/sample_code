#include<stdio.h>
#include<iostream>
#include<string>
#include<typeinfo>
using namespace std;

int main(void){

string str1 = "hello ";
string str2 = "world";
string str3 = str1 + str2;


cout << str3.size() << endl;

int size = str3.size();

for (int i = 1; i <= size/2; i++){
	char temp_start = str3[i-1];
	char temp_end = str3[size-i];
	str3[i-1] = temp_end;
	str3[size-i] = temp_start;
}
cout << str3 << endl;


return 0;
}

