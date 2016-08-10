#include <iostream>
#include "CppRoutines.hpp"

//////////////////////////////////////////VECTOR

//Default Constructor
template<typename T>
Vector<T>::Vector(){
	size = 3;
	data = new T[size];
}

//Constructor by dimension
template<typename T>
Vector<T>::Vector(int k):size(k){
	data = new T[size];
}

//Set Vector element
template<typename T>
void Vector<T>::__setitem__(int i, T eVect){
	if (i<size && i>=0)
		data[i] = eVect;
}

//Get Vector element with []
template<typename T>
T Vector<T>::__getitem__(int i){
	if (i < size && i >= 0)
		return data[i];
	T nul = 0;
	return nul;
}

//Print Vector data
template<typename T>
const char *Vector<T>::__repr__(){
	for(int i=0; i<size; i++){
		std::cout<<data[i]<<" ";
	}
	return "";
}

//Replace Vector data
template<typename T>
void Vector<T>::copy(const Vector &Vect){
	if (size == Vect.size)
		for (int i=0; i<size; i++)
			data[i] = Vect.data[i];	
}

//Get Vector element 
template<typename T>
T Vector<T>::get(int n){
	if (n < size && n >= 0) 
		return data[n];
}

//Find Maximum
template<typename T>
T Vector<T>::max(){
	T temp = data[0];
	for (int i=1; i<size; i++)
		if (data[i]> temp)
			temp = data[i];
	return temp;
}

//Sum
template<typename T>
T Vector<T>::sum(){
	T temp = data[0];
	for (int i=1; i<size; i++)
		temp += data[i];
	return temp;
}

//Get Vector dimension
template<typename T>
int Vector<T>::length(){
	return size;
}

//Vector Operations
template<typename T> //dot product
T Vector<T>::operator*(const Vector& Vect)  const{
    if (size != Vect.size){
        std::cout << "Invalid, dimensions do not match!" << std::endl;
        return 0;
    }
    T sum = 0;
    for (int i = 0; i < size; i++){
        sum = sum + data[i] * Vect.data[i];
    }
    return sum;
}

template<typename T>//scalar and vector product
Vector<T> Vector<T>::operator*(const T scalar) const{
	Vector res(size);
    for (int i=0; i<size; i++) 
		res.data[i] = data[i] * scalar;
    return res;
}

template<typename T>
Vector<T> Vector<T>::operator-(const Vector &Vect) const{
	Vector res(size);
    for (int i=0; i<size; i++) 
		res.data[i] = data[i] - Vect.data[i];
    return res;
}

template<typename T>//scalar and vector quotient
Vector<T> Vector<T>::operator/(const T scalar) const{
	Vector res(size);
    for (int i=0; i<size; i++) 
		res.data[i] = data[i] / scalar;
    return res;
}

//Instantiate template classes
template class Vector<int>;
template class Vector<double>;


//////////////////////////////////////////MATRIX


//Default Constructor
template<typename T>
Matrix<T>::Matrix(){
	rowi = 3;
	colj = 3;
	data = new T [rowi*colj];
}

//Constructor by dimension
template<typename T>
Matrix<T>::Matrix(int r, int c):rowi(r), colj(c){
	data = new T [rowi*colj];
}

//Print Matrix data
template<typename T>
const char *Matrix<T>::__repr__(){
	for(int i=0; i<rowi*colj; i++){
		std::cout<<data[i]<<" ";
		if((i+1)%colj == 0)
			std::cout<<"\n";
	}
	return "";
}

//Set Matrix element
template<typename T>
void Matrix<T>::__setitem__(int index, T eMat){
	if (index<rowi*colj && index>=0)
			data[index] = eMat;
}

//Get Matrix element with []
template<typename T>
T Matrix<T>::__getitem__(int index){
	if (index < rowi*colj && index >= 0)
			return data[index];
	T nul = 0;
	return nul;
}

//Replace Matrix data
template<typename T>
void Matrix<T>::copy(const Matrix &Mat){
	if (rowi*colj == Mat.rowi*Mat.colj)
		for (int i=0; i<rowi*colj; i++)
			data[i] = Mat.data[i];	
}

//Get Matrix row size
template<typename T>
int Matrix<T>::rowsize(){
	return rowi;
}

//Get Matrix column size
template<typename T>
int Matrix<T>::colsize(){
	return colj;
}

//Matrix Operations
template<typename T> //matrix and row vector product
Vector<double> Matrix<T>::operator*(const Vector<double> &Vect) const{
    if (colj != Vect.size){
        std::cout << "Invalid, dimensions do not match! "; 
		return Vect;
    }
    Vector<double> res(colj);
	for(int i=0; i<colj; i++)
		res.data[i]=0;
	int row=0;
    for (int i=0; i<rowi; i++){
		for (int j=0; j<colj; j++){
			res.data[i] = res.data[i] + data[row] * Vect.data[j];
			row++;
		}
    }
    return res;
}

template<typename T>//scalar and matrix product
Matrix<T> Matrix<T>::operator*(const T scalar) const{
	Matrix res(rowi, colj);
    for (int i = 0; i < rowi*colj; i++) res.data[i] = data[i] * scalar;
        return res;
}

//Instantiate template classes
template class Matrix<int>;
template class Matrix<double>;