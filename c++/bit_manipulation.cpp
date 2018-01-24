#include<stdio.h>
#include<iostream>
#include<string>
#include<typeinfo>
#include<map>

using namespace std;

int mult_by_pow_2(int number, int power)
{
    return number<<power;
}

int div_by_pow_2(int number, int power)
{
    return number>>power;
}

int bitwiseCOMP(int number1){
	return ~number1;
}

int bitwiseAND(int number1, int number2){
	return number1 & number2;
}

int bitwiseOR(int number1, int number2){
	return number1 | number2;
}

int bitwiseXOR(int number1, int number2){
	return number1 ^ number2;
}

void displayBitWiseCOMP(int number1){
	for (int i=0; i<number1; i++){
			cout << i << " COMP = " << bitwiseCOMP(i)<< endl;
	}
}

void displayBitWiseAND(int number1, int number2){
	for (int i=0; i<number1; i++){
		for (int j=0; j<number2; j++){
			cout << i << " AND " << j << " = " << bitwiseAND(i, j) << endl;
		}
	}
}

void displayBitWiseOR(int number1, int number2){
	for (int i=0; i<number1; i++){
		for (int j=0; j<number2; j++){
			cout << i << " OR " << j << " = " << bitwiseOR(i, j) << endl;
		}
	}
}

void displayBitWiseXOR(int number1, int number2){
	for (int i=0; i<number1; i++){
		for (int j=0; j<number2; j++){
			cout << i << " XOR " << j << " = " << bitwiseXOR(i, j) << endl;
		}
	}
}

void setBit(int number, int bitPos){
	number |= (1<<bitPos);
	cout << "SetBit: " << number << endl;
	//     0011 = 3
	//  OR 0100 = 4
	//  =  0111 = 7  

}

void clearBit(int number, int bitPos){
	number &= ~(1<<bitPos);
	cout << "ClearBit: " << number << endl;
	// 	   0001
	// <<  0010 = 2
	// ~   1101 = 4
	// &   0011 = 7  
	// =   0001 = 1
}

void toggleBit(int number, int bitPos){
	number ^= (1<<bitPos);
	cout << "ToggleBit: " << number << endl;
	//     0001 = 1
	// XOR 0011 = 3
	//  =  0010 = 2  
}


void checkBit(int number, int bitPos){
	int bit = (number >> bitPos) & 1;
	cout << "CheckBit: " << bit << endl;

	// NUM 0011 = 3
	// >>2 0000 = 0
	// AND 0001 = 1
	// =   0000 = 0  
}

void changeBit(int number, int bitPos, int bitVal){
	number = number & ~(1 << bitPos) | (bitVal << bitPos);
	cout << "ChangeBit: " << number << endl;

	// NUM 0011 = 3

	// <<2 0001
	// CMP 0100 = 0
	// =   1011 = 1
	
	// AND 0011 = 0 

	//     0001
	// <<  0100

	// OR  0111 = 7 
}


int main (void){

	int a = 1;
	int b = 1;
	cout << mult_by_pow_2(7, 2) << endl;
	cout << div_by_pow_2(28, 2) << endl;
	int number1 = 10;
	int number2 = 10;
	//displayBitWiseCOMP(number1);
	//displayBitWiseAND(number1, number2);
	//displayBitWiseOR(number1, number2);
	//displayBitWiseXOR(number1, number2);
	setBit(3, 2); //0011=3. Take 1 (0001 and shift it 2 positions to left)
	clearBit(3, 1); //0011=3. Take 1 (0001 and shift it 1 positions to left and comp it so u can & it)
	toggleBit(3, 0); //0011=3. 
	checkBit(3, 1); //0011=3. 
	changeBit(3, 2, 1);
	return 0;
}
// 000001 1
// 000010 2
// 000100 4
// 001000 8
// 010000 16

// left shift = multiply by 2
// rignt snift = multiply by 2
// 000111 7
// 001110 14
// 011100 28

