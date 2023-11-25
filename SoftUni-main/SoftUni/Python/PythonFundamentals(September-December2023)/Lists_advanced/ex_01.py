data0 = input().split(', ')
data1 = input().split(', ')
new_data =[]
for first in data0:
    for second in data1:
        if first in second:
            new_data.append(first)
            break
print(new_data)