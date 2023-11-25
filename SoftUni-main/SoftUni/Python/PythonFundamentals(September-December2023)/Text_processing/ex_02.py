data = input().split()
total_sum = 0

if len(data[0]) > len(data[1]):
    for i in range(len(data[1])):
        total_sum += ord(data[0][i]) * ord(data[1][i])
    for i in range(len(data[1]), len(data[0])):
        total_sum += ord(data[0][i])
elif len(data[1]) > len(data[0]):
    for i in range(len(data[0])):
        total_sum += ord(data[0][i]) * ord(data[1][i])
    for i in range(len(data[0]),len(data[1])):
        total_sum += ord(data[1][i])
else:
    for i in range(len(data[0])):
        total_sum += ord(data[0][i]) * ord(data[1][i])

print(total_sum)