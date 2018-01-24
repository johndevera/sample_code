#include<stdio.h>
#include<iostream>
#include<math.h>
using namespace std;

int main(void){


int number = 43673;
int power = 2;
int mod = 10;
// cout << "Enter in a number: ";
// cin >> number;

// cout << "Enter in a digit: ";
// cin >> digit;

int x = number%mod;
cout << "x = " << x << endl;
int p = pow(10, power);
cout << "p = " << p << endl;
x = (number/p)%10;

cout << x << endl;


return 0;
}