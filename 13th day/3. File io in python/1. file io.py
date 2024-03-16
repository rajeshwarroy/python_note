# Before we can perform any operation on a file, we must first open it. python provides the open() function to open a file.
# it take to arguments: the name of the file and file mode in which the file should bo opened.
# the mode can be 'r' for reading, 'w' for writing, or 'a' for appending.


# f = open('myfile.txt', 'r')
f = open('myfile.txt')             # 'r' manea 'reading' ['r' mode default hoyea thakea,
# print(f)
test = f.read()             # 'f.read()' ar madhomea "text file" ar "contain" takea "read" korea neaoya hoyeachea. [Extract korea niyeachea]
print(test)
f.close()                   # file close.
