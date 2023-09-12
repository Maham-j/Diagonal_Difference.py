# Import math module for calculations
import math  
import os  
import random  
import re  
import sys  

def diagonalDifference(arr):
    # Initialize variables to track diagonal sums
    primary_diagonal = 0
    secondary_diagonal = 0
    
    # Loop through the matrix
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')  # Print matrix element
        print()
        primary_diagonal += arr[i][i]  # Sum elements on primary diagonal
        secondary_diagonal += arr[i][n-i-1]  # Sum elements on secondary diagonal
    
    # Calculate absolute difference between diagonal sums
    result = abs(primary_diagonal - secondary_diagonal)
    return result

if __name__ == '__main__':
    
    n = int(input().strip())  # Read matrix size
    
    arr = []
    
    # Read matrix elements and store in array
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    result = diagonalDifference(arr)  # Calculate diagonal difference
    
    print(result)
