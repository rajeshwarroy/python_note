a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
for i in range(1, 11):                      # range 1 taheaka start hobea, and 10 porjonto cholbea, but 11 print hobeana.
    print(f"{a} X {i} = {a*i}")             # akhanea "number" gulo por por sum hobea.
    print(f"{int(a)} X {int(i)} = {int(a)*int(i)}")         # "range" and "input" number gun hobea
    print('\n')                             # line gape hobea loop joto bar cholbea toto bar.



