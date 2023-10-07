def perfect_num(a: int):
    divisors = []
    for i in range (1, a):
        if a%i == 0:
            divisors.append(i)
    if sum(divisors)!=a or a<0:
        message = "It's not so perfect."
    else:
        message = "We have a perfect number!"
    return message

num = int(input())
print(perfect_num(num))