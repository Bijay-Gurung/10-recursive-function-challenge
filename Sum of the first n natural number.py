def sum_of_natural_number(n):
    if n==0:
        return 0
    else:
        return n+sum_of_natural_number(n-1)
result = sum_of_natural_number(5)
print(result)