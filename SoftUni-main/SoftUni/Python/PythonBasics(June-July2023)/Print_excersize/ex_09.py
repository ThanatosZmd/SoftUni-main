length = int(input())/10
width = int(input())/10
heigth = int(input())/10
procent = int(input())/100
volume_liters = length*width*heigth
needed = volume_liters*(1-procent)
print(needed)