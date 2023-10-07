def odd_and_even_sum(a: int):
    odd_sum = 0
    even_sum = 0
    while a>0:
        x = a%10
        if x%2==0:
            even_sum+=x
        else:
            odd_sum+=x
        a//=10
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

odd_and_even_sum(int(input()))