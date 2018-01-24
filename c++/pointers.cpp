#include<stdio.h>
#include<iostream>

using namespace std;

void passByReference(int &particle_value){
	int *p_particle_value = &particle_value;
	*p_particle_value += 2;
}

int passByValue(int particle_value){
	particle_value += 3;
	return particle_value;
}

int main (void) {

int particle_value = 23;
int *p_particle_value = &particle_value;
cout << *p_particle_value << endl;
cout << &particle_value << endl;
cout << particle_value << endl;

passByReference(particle_value);
cout << "Pass by reference: " << particle_value << endl;

int pbv = passByValue(particle_value);
cout << "Pass by value: " << pbv << endl;




int sherlock = 221;
int *p_sherlock = &sherlock;
cout << "*p " << *p_sherlock << endl;

passByReference(sherlock);
cout << "PBR " << sherlock << endl;


return 0;
}