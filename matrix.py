import numpy as np
class matrix:
    matrices=[]

    
    def mat(self):
  
        for i in range(2):
            
            rows=int(input(f"enter number of rows for matrix {i+1} "))        
            col=int(input(f"enter number of column for matrix {i+1} "))
            
            print("enter values:")
            while True:
                val=list(map(int,input().split()))    
                if len(val)!=rows*col:
                    print("values doesn't match size !")
                else:
                    break
            
            matrix.matrices.append(
                np.array(val).reshape(rows,col)
            )
        

    def mat2(self):
           
        rows=int(input(f"enter number of rows for matrix: "))        
        col=int(input(f"enter number of column for matrix: "))
        print("enter values:")
        while True:
            val=list(map(int,input().split()))    
            if len(val)!=rows*col:
                print("values doesn't match size !")
            else:
                break
            
        matrix.matrices.append(
           np.array(val).reshape(rows,col)
        )
            
    def addition(self):
        try:
            res=np.add(matrix.matrices[0],matrix.matrices[1])
            print(f"result of addition :\n{res}")
        except Exception as e:
            print(f"Error : {e}")
        else:
            return res
     

    def subtraction(self):
        try:
            res=np.subtract(matrix.matrices[0],matrix.matrices[1])
            print(f"subtraction of matrix:\n{res}")
        except Exception as e:
            print(f"Error : {e}")
        else:
            return res
       
    def multiply(self):
        try:
            res=np.dot(matrix.matrices[0],matrix.matrices[1])
            print(f"multiplication of matrix:\n{res}")
            
        except Exception as e:
            print(f"Error : {e}")
        else:
            return res
     
    
    def transpose(self):
        try:
            res=matrix.matrices[0].T
            print(f"Transpose of matrix:\n{res}")
        except Exception as e:
            print(f"Error : {e}")
        else:
            return res

    
    def determinant(self):
        try:
            res=np.linalg.det(matrix.matrices[0])
            print(f"Determinant of matrix:\n{res}")
        except Exception as e:
            print(f"Error : {e}")
        else:
            return res
        

    def inverse(self):
        try:
            res=np.linalg.inv(matrix.matrices[0])
            print(f"Inverse of matrix:\n{res}")
        except Exception as e:
            print(f"Error : {e}")
        else:
            return res
  


print("----------MATRIX CALCULATOR------------")
#swich case
while True:
    print("Enter operation you need to perforn")
    print("1.Addition \n2.Subtraction \n3.Multiplication \n4.Transpose \n5.Determinant \n6.Inverse \n7.Exit ")
    ch=int(input("Enter choice:"))


    m=matrix()
    if ch==1:
        # n=input("Enter number of matrix you want to add:")
       
        m.mat()
        m.addition()
             
        matrix.matrices.clear()
        # break
    
    elif ch==2:

        m.mat()
        m.subtraction()
        matrix.matrices.clear()
        # break

    elif ch==3:

        m.mat()
        m.multiply()
        
        matrix.matrices.clear()
        # break

    elif ch==4:

        m.mat2()
        m.transpose()
        
        matrix.matrices.clear()
        # break

    elif ch==5:

        m.mat2()
        m.determinant()
        
        matrix.matrices.clear()
        # break

    elif ch==6:

        m.mat2()
        m.inverse()
    
        matrix.matrices.clear()
        # break
    
    elif ch==7:
        print("Terminating program!!!")
        break

    else:
        print("Invalid Choice")
        break



      

