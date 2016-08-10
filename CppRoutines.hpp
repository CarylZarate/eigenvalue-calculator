#ifndef CppRoutines_hpp
#define CppRoutines_hpp

#include <stdio.h>
#include <iostream>

template<typename T>
class Vector{
public:
	T *data;
	int size;

	Vector();
	Vector(int size);
	void __setitem__(int i, T eVect);
	T __getitem__(int i);
	const char *__repr__();
	void copy(const Vector &Vect);
	T get(int n);
	T max();
	T sum();
	int length();
	T operator*(const Vector& Vect)  const;
	Vector<T> operator*(const T scalar) const;
	Vector<T> operator-(const Vector &Vect) const;
	Vector<T> operator/(const T scalar) const;
};

template<typename T>
class Matrix: public Vector<double>{
public:
	T *data;
	int rowi;
	int colj;
	
	Matrix();
	Matrix(int r, int c);
	const char *__repr__();
	void __setitem__(int index, T eMat);
	T __getitem__(int index);
	void copy(const Matrix &Mat);
	int rowsize();
	int colsize();
	Vector<double> operator*(const Vector<double> &Vect) const;
	Matrix<T> operator*(const T scalar) const;
};
#endif
