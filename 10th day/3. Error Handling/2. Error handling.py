a = input("Enter any keyword: ")
print(f"Multiplication table of {a} is: ")

# program end or error janooo na asea tar jonno try use kora hoyea thakea. jeano program run thaktea parea.
# example: program "integer" diyea kor holea input "integer" ar bodolea "string" input diyea thaklea seai program error dekhabea.
# ar jonnoy "try" use hoyea thakea. jeano program run thakea error kea skip kora jeano cholea.

try:                       # "try" ar 1st a for loop dekbea, run hoy kina, error hoylea, ""except"" ar kachea pathay dibea
    for i in range(1, 11):                      # range 1 taheaka start hobea, and 10 porjonto cholbea, but 11 print hobeana.
        # print(f"{a} X {i} = {a*i}")             # akhanea "number" gulo por por sum hobea.
        print(f"{int(a)} X {int(i)} = {int(a)*int(i)}")         # "range" and "input" number gun hobea
        print('\n')                             # line gape hobea loop joto bar cholbea toto bar.
except Exception as error:                      # 1st part/ for loop na chollea "except" run hobea.
    print("Sorry, Invalid Input! ")


print('\n')
print("some Important line of code")
print("End of program")






print('\n')
try:
    num = int(input("Enter an integer: "))          # Target  number ditea parlea, number print hobea,
    a = [6, 3]                                      # target number 1 or 0 dilea, program run hobea.
    print(a[num])
except ValueError:                                  # error number/intger dilea ati run hobea.
    print("Number entered is not an integer.")

except IndexError:                                  # string dilea ayta run hobea
  print("Index Error")
