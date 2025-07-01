# app/calculator.py
# this is siraj and this commit should get merged hopely 
# this is test for wrong commit push hopely

def add(a, b):
    return a + b+1 

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


