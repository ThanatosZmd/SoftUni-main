data = input().split("\\")
name, extension = data[len(data)-1].split(".")
print(f"File name: {name}\nFile extension: {extension}")