import CppRoutines

print "testing example"

#defines vector of size 3
A = CppRoutines.Vectori()  #int
A = CppRoutines.Vectord(3) #double
B = CppRoutines.Vectord(3)

#defines a 3x3 matrix
C = CppRoutines.Matrixi()
C = CppRoutines.Matrixd(3,3)

#print elements of A
print "A is "
print A
print "B is "
print B
print "C is "
print C

#set elements of A
A[0] = 0.0
A[1] = 1.0
A[2] = A[1]
print "A is "
print A

#set elemens of C
C[0] = 2
C[2] = 1
C[4] = 0
print "C is"
print C

print "C.rowsize"
print C.rowsize()
print "C.colsize"
print C.colsize()

print "C*A"
print C*A

print "C*2"
print C*2

print "copy A to B"
B.copy(A)
print "B is "
print B

print "B.get(1)"
print B.get(1) 

print "B.max()"
print B.max()

print "B.sum()"
print B.sum()

print "B.length"
print B.length()

print "A*B"
print A*B

print "A*2"
print A*2
A=A*2
print "A-B"
print A-B

print "B-2"
print B/2
