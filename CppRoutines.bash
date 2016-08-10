#\!/bin/bash -f

swig -python -c++ CppRoutines.i

g++ -c CppRoutines.cpp CppRoutines_wrap.cxx -I/python27/include
	
g++ -shared CppRoutines.o CppRoutines_wrap.o -L/python27/libs -lpython27 -o _CppRoutines.pyd