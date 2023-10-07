def add_and_subtract(a, b, c):
    def sum_numbers(a,b):
        return a+b
    def subtract(a,b,c):
        return sum_numbers(a,b)-c
    return subtract(a,b,c)
print(add_and_subtract(int(input()),int(input()),int(input())))