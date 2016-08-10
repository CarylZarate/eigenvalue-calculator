 %module CppRoutines
 %{
 /* Includes the header in the wrapper code */
 #include "CppRoutines.hpp"
 %}
 
 /* Parse the header file to generate wrappers */
 %include "CppRoutines.hpp"
 
 %template(Vectori) Vector<int>;
 %template(Vectord) Vector<double>;
 %template(Matrixi) Matrix<int>;
 %template(Matrixd) Matrix<double>;