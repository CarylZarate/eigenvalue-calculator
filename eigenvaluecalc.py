from Tkinter import *
from tkMessageBox import *
from random import random
import numpy
import time
import CppRoutines

class MainWindow:
    
    #Creates the GUI       
    def __init__(self, master):
        mainframe = Frame(master)
        mainframe.pack()
        
        self.Space = Label(mainframe, text = "   ")
        self.Space.grid(row=0)        
                
        self.Parameters = Label(mainframe, text = "PARAMETERS")
        self.Parameters.grid(row=1, columnspan=3)        
        
        self.SizeLabel = Label(mainframe, text = "Enter the size of the matrix:")
        self.SizeLabel.grid(row=2)
        
        self.SizeEntry = Entry(mainframe)
        self.SizeEntry.insert(END, '100') 
        self.SizeEntry.grid(row=3)
              
        self.eLabel = Label(mainframe, text = "Epsilon:")
        self.eLabel.grid(row=4)
        
        self.eEntry = Entry(mainframe)
        self.eEntry.insert(END, '0.001')
        self.eEntry.grid(row=5)
        
        self.Div = Label(mainframe, text = "    ")
        self.Div.grid(row=6)
        
        self.MethodLabel = Label(mainframe, text = "METHOD")
        self.MethodLabel.grid(row=7, columnspan=3)
        
        self.Method = IntVar()        
        
        self.WithNumpy = Radiobutton(mainframe, text="Solve with Numpy",value=1, variable = self.Method, command=self.printMessage)
        self.WithNumpy.grid(row=8, columnspan=3)
        
        self.WithoutNumpy = Radiobutton(mainframe, text="Solve without Numpy",value=2, variable = self.Method, command=self.printMessage)
        self.WithoutNumpy.grid(row=9, columnspan=3)

        self.WithoutNumpy = Radiobutton(mainframe, text="C++ Routines",value=3, variable = self.Method, command=self.printMessage)
        self.WithoutNumpy.grid(row=10, columnspan=3)
        
        self.Solve = Button(mainframe, text="Solve", command=self.solveEigen)
        self.Solve.grid(row=11)
        
        self.EigenvalueLabel = Label(mainframe, text = 'Eigenvalue:')
        self.EigenvalueLabel.grid(row=12)
        
        self.Eigenvalue = Label(mainframe, text = ' ')
        self.Eigenvalue.grid(row=13)
        
    #Prints the method selected   
    def printMessage(self):
        if self.Method.get()==1:
            print 'With numpy'
        elif self.Method.get()==2:
            print 'Without numpy'
        elif self.Method.get()==3:
            print 'C++ routines'
        else:
            print self.Method.get()
            print 'Error'
    
    #Checks if the parameter entries are valid and if a method was chosen
    def solveEigen(self):
        Size = 100        
        temp = self.SizeEntry.get()
        try:        
            if temp:      
                Size = int(temp)
                print Size
                self.SizeLabel.configure(text = 'Enter the size of the matrix:')
        except ValueError:
            print 'Invalid entry: ' + temp
            print 'Using default value'
            self.SizeLabel.configure(text='Invalid entry, use default value: Size=100')
        Eps = 0.001
        temp = self.eEntry.get()
        try:
            if temp:
                Eps = float(temp)
                print Eps
                self.eLabel.configure(text='Epsilon:')
        except ValueError:
            print 'Invalid entry: ' + temp
            print 'Using default value'
            self.eLabel.configure(text='Invalid entry, use default value: Eps=0.001')
        
        if self.Method.get() == 1:
            self.solveNumpy(Size, Eps)
        elif self.Method.get() == 2:
            self.solveNotNumpy(Size, Eps)
        elif self.Method.get() == 3:
            self.CppRout(Size, Eps)
        else:
            self.Eigenvalue.configure(text='Select a method')
    
    #Solves the eigenvalue and eigenvector with Numpy        
    def solveNumpy(self, size, eps):
        #Record the time        
        startTime = time.time()         
        # Initial Guess
        guess_x0 = numpy.ones(size, float)

        #Generate random matrix
        matrix_A= numpy.random.randn(size,size)     
        
        # Power Method with NumPy
        iter_counter = 0
        iter_counter_lim = 100;
        while iter_counter < iter_counter_lim:
            guess_x1=numpy.zeros(size)    
            if (numpy.sqrt(sum(guess_x1-guess_x0)**2/len(guess_x1)) < eps):
                print 'breaking'                
                break
            guess_x0 = numpy.dot(matrix_A, guess_x0)
            guess_x1 = guess_x0/max(guess_x0)
            iter_counter+=1    
        print 'number of iterations is ' + str(iter_counter)
        print 'The eigenvector is '
        print guess_x1

        #Solve for eigenvalue
        eigenvalue = numpy.dot(numpy.dot(matrix_A, guess_x0), guess_x0)/numpy.dot(guess_x0,guess_x0)
        print 'The eigenvalue is '
        print eigenvalue
        print 'Runtime is ' + str(time.time()-startTime)
        self.showAnswer(eigenvalue)      
    
    #Solves the eigenvalue and eigenvector without Numpy 
    def solveNotNumpy(self, size, eps):
        #Record the time
        startTime = time.time()
        # Initial Guess
        guess_x0 = numpy.ones(size, float)
        #Generate random matrix
        matrix_A= numpy.random.randn(size,size)
        
        # Define breaking condition
        iter_counter_lim = 100

        # Power Method with nested for loops
        iter_counter = 0
        while iter_counter < iter_counter_lim:
            temp_vect = range(size)  
            for i in range(size):
                temp=0        
                for j in range(size):
                    temp = temp + guess_x0[j] * matrix_A[i][j]
                temp_vect[i] = temp
            norm = max(temp_vect)
            for i in range(size):
                temp_vect[i] = temp_vect[i]/norm
            iter_counter+=1
            #Check tolerance    
            s=0
            for i in range(size):
                s = s+(guess_x0[i]-temp_vect[i])**2
    
            err = numpy.sqrt(s/size)
    
            if err<eps:
                break
    
            guess_x0 = temp_vect
            
        print 'number of iterations is ' + str(iter_counter)
        print 'The eigenvector is '
        print guess_x0

        #Eigenvalue with nested for loops
        temp_vect1 = range(size)
        for i in range(size):
            temp = 0
            for j in range(size):
                temp = temp + guess_x0[j] * matrix_A[i][j]
            temp_vect1[i] = temp
        temp_vect2 = range(size)
        for i in range(size):    
            temp_vect1[i] = temp_vect1[i] * guess_x0[i]
            temp_vect2[i] = guess_x0[i] * guess_x0[i]

        temp1=0
        temp2=0
        for i in range(size):
            temp1 += temp_vect1[i]
            temp2 += temp_vect2[i]
        eigenvalue = temp1/temp2

        print 'The eigenvalue is '
        print eigenvalue 
        print 'Runtime is ' + str(time.time()-startTime)
        self.showAnswer(eigenvalue)
    
    #Solves the eigenvalue and eigenvector with C++ routines
    def CppRout(self, size, eps):
        #Record the time
        startTime = time.time()
        #Initial Guess
        guess_x0 = CppRoutines.Vectord(size)
        for i in range(size):
            guess_x0[i]=1.0
        #Generate random matrix
        matrix_r = numpy.random.randn(size,size)
        matrix_A = CppRoutines.Matrixd(size,size)
        k=0
        for i in range(size):
            for j in range(size):
                matrix_A[k] = matrix_r[i][j]
                k+=1			
        #Define breaking condition
        iter_counter_lim = 100	
        #Power Method
        iter_counter = 0
        while iter_counter < iter_counter_lim:
            guess_x1 = CppRoutines.Vectord(size)
            for i in range(size):
                guess_x1[i]=0.0
            if (numpy.sqrt((guess_x1-guess_x0).sum()**2/size)<eps):
                print 'breaking'
                break
            guess_x0 = matrix_A*guess_x0
            guess_x1 = guess_x0/guess_x0.max()
            iter_counter+=1
        print 'number of iterations is ' + str(iter_counter)
        print 'The eigenvector is '
        print guess_x1
        #Solve for eigenvalue
        eigenvalue = (matrix_A*guess_x0)*guess_x0/(guess_x0*guess_x0)
        print 'The eigenvalue is '
        print eigenvalue
        print 'Runtime is ' + str(time.time()-startTime)
        self.showAnswer(eigenvalue)
			
	
    #Shows the eigenvalue on the MainWindow    
    def showAnswer(self, eig):
        eigen = str(eig)
        print eigen
        self.Result = self.Eigenvalue.configure(text=eigen)
    
root = Tk()
root.title("Eigenvalue & Eigenvector Calculator")
root.geometry('275x320')
b=MainWindow(root)
root.mainloop()
