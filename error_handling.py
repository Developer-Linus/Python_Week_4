filename = input("Please input the name of the file with its extension:")
try:
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file {filename} was not found.")
except PermissionError:
    print(f"Permission denied: unable to read the file {filename}. Please check the file permissions.")

