file_name = 'hello.txt'

# FILE READING
f = open(file_name, 'r')
content = f.read()
print(content)

# FILE WRITING - REPLACING THE WHOLE TEXT
f = open(file_name, 'w')
f.write('Hello Kids')

f = open(file_name, 'r')
print(f.read())

# FILE APPENDING - END OF FILE
f = open(file_name, 'a')
f.write('\nThis line was added later!')

f = open(file_name, 'r')
print(f.read())