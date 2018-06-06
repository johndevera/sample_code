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

// int i[] = {1,2,3,4};
// int *p = &i[2];
// std::cout << p[-1] << std::endl;

std::vector<int> v;
int i; 
while (std::cin >> i)
	v.push_back(i);

for( int i = 0; i < v.size() -1; ++i){
	std::cout << v[i] << " " << v[i+1] << std::endl;
}





return 0;
}