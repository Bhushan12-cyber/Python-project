import numpy as np
# 1. Matrix and Vector Operations
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([1, 2, 3])
#Vector and Matrix Multiplication
print("Multiplication of vector and matrix is:\n ",A * B)
#Trace or diagonal sum of A
trace = np.trace(A)
print("Trace of A : ",trace)
#or by another method
sum = 0
for i in range(len(A)):
  sum += A[i][i]
print("Diagonal Sum : ",sum)
#eigenvalue , eigenvector
eigenvalue , eigenvector = np.linalg.eig(A)
print("Eigenvalue :\n",eigenvalue)
print("Eigenvector :\n",eigenvector)
#Replace
A[2] = [10,11,12]
#Determinant
det = np.linalg.det(A)
print("Determinant : ",det)
#if singular or not
print("matrix is","not singular" if det != 0 else "singular")



# 2. Invertibility of Matrices
# Verify the invertibility of the updated matrix A
if det != 0:
  print("Inverse of matrix A:\n",np.linalg.inv(A))
else:
  print("Matrix is singular")
# linear equations A x X = B
try:
  X = np.linalg.solve(A, B)
  print("\nSolution X of A x X = B:\n", X)
except np.linalg.LinAlgError as e:
  print("Error")
# 3. Practical Matrix Operations
C = np.random.randint(1,21,size = (4,4))
print(C)
#rank 
rank = np.linalg.matrix_rank(C)
print("Rank of C : ",rank)
#submatrix
submatrix = C[:2,-2:]
print("Submatrix of C :",submatrix)
# Frobenius norm
frob = np.linalg.norm(C,'fro')
print("Frobenius norm :" ,frob)
#Multiplcation of A and C

try:
  C_trim = C[:3,-3:]
  print("Multiplication :\n ",A @ C_trim)
except ValueError as e:
  print("Error",e)

# 4. Data Science Context
D = np.array([[3, 5, 7, 9, 11],
              [2, 4, 6, 8, 10],
              [1, 3, 5, 7, 9],
              [4, 6, 8, 10, 12],
              [5, 7, 9, 11, 13]])
#standardized
d_mean = np.mean(D)
d_std = np.std(D)
d_stdized = (D - d_mean)/d_std
print("Standardized D:\n ",d_stdized) 
#covariance matrix
cov_d = np.cov(d_stdized.T)
print("Covariance matrix:\n ",cov_d)
#eigenvalue and eigenvector of D
eigen_d,vector_d= np.linalg.eig(cov_d)
print("Eigenvalues :\n ",eigen_d )
print("Eigenvector:\n ",vector_d)
#reduce to 2
sort_ind  = np.argsort(eigen_d)[::-1]
top_2_vectors = vector_d[:, sort_ind[:2]]
d_pca = d_stdized @ top_2_vectors
print("D reduced to 2 principal components:\n", d_pca)