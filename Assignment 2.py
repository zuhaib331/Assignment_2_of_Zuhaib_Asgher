# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 17:37:21 2018

@author: Zuhaib Asghar
"""
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

def is_identity_matrix(matrix):
    n = len(matrix)
    if n != len(matrix[0]):
        return False
    for i in range(n):
        for j in range(n):
            if i == j:
                if matrix[i][j] != 1:
                    return False
            else:
                if matrix[i][j] != 0:
                    return False
    return True

print(is_identity_matrix(X))