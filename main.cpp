#include<iostream>
#include "CppRoutines.hpp"

int main(){
	Vector<int> A;
	std::cout<<A.length();
	
	Vector<double> B(3);
	Matrix<double> C(3,3);
	std::cout<<C.colsize();
	
	for (int i=0; i<B.length(); i++)
	B.data[i] = 1;
	
	for (int i=0; i<C.rowsize()*C.colsize(); i++)
		C.data[i] = 2;
	
	C = C*0.5;
	B = B*2;
	B = B/2;
	B = C*B;
	double p = B.sum();
	p = B.max();
	A = A-A;
	p = B*B;
	
	return(1);
}