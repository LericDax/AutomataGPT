# This file contains the code for the Math Agent

import numpy as np

def evaluate_expression(expression):
    '''This function takes in a mathematical expression in the form of a string and returns the result'''
    result = eval(expression)
    return result


def vector_addition(v1, v2):
    '''This function takes in two vectors in the form of numpy arrays and returns their sum'''
    return np.add(v1, v2)


def vector_subtraction(v1, v2):
    '''This function takes in two vectors in the form of numpy arrays and returns their difference'''
    return np.subtract(v1, v2)


def scalar_multiplication(scalar, v1):
    '''This function takes in a scalar and a vector in the form of a numpy array and returns the result of the scalar multiplication of the vector provided'''    
    return np.multiply(scalar, v1)


def recursion_factorial(num):
    '''This function returns the factorial of a number using recursion'''    
    if num == 0:
        return 1
    return num * recursion_factorial(num-1)