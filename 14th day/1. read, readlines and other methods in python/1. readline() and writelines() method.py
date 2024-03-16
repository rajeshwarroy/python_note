# readline() method keano banano hoy?
# readline banano hoy jano line by line kuno file read kortea pari ay jonno.



# f = open('myfile.txt', 'r')       # "r" manea "Reading"
# while True:
#   line = f.readline()             # readline()  ar madhomea "text file" ar "contain" takea "read" korea neaoya hoyeachea. [Extract korea niyeachea]
#   if not line:                    # jodi ar line na thakea
#     break
#   print(line)                     # "txt" file ar text print korbea



# f = open('myfile.txt', 'r')         # "r" manea "Reading"
# while True:
#     line = f.readline()             # readline()  ar madhomea "text file" ar "contain" takea "read" korea neaoya hoyeachea. [Extract korea niyeachea]
#     print(line)                     # "txt" file ar text print korbea.
#     if not line:                    # jodi ar line na thakea
#         print(line, type(line))     # file ta kun type ar ta print korbea.
#         break




f = open('myresults.txt', 'r')                      # "r" manea "Reading"
i = 0
while True:
  i = i + 1
  line = f.readline()                               # readline()  ar madhomea "text file" ar "contain" takea "read" korea neaoya hoyeachea. [Extract korea niyeachea]
  if not line:
    break
  m1 = int(line.split(",")[0])                      # "int" diyea intger korea nichea sob, "".split()"" separator, default separator is any whitespace.
  m2 = int(line.split(",")[1])
  m3 = int(line.split(",")[2])
  print(f"Marks of student {i} in Maths is: {m1*2}")        # "m1*2 kora hoyeachea.
  print(f"Marks of student {i} in English is: {m2*2}")
  print(f"Marks of student {i} in SST is: {m3*2}")

  print(line)




f = open('myfile2.txt', 'w')                    # "w" = writing; file open kora hoy, ay name a file na thaklea create korea naoya hoy.
lines = ['line 1\n', 'line 2\n', 'line 3\n']    # 'line 1\n', 'line 2\n', 'line 3\n' manea, line create hoyeachea and porear line a cholea geachea, 3ta line creat hoyeachea.
f.writelines(lines)                             # "writelines method" use kora hoyeachea.
f.close()                                       # bondho korar jonno use kora hoy.
