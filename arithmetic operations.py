def arithmetic_operations(a,b):
    sum = a + b
    difference = a - b
    product = a * b
    quotient = a / b if b != 0 else None
    return sum,difference,product,quotient
a = int(input("Enter frist number:"))
b = int(input("Enter second number:"))
result=arithmetic_operations(a,b)
sum,difference,product,quotient=result
print(f"Sum:{sum} Difference:{difference} Product:{product} Quotient:{quotient}")
