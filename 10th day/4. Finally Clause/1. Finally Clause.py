#


def func1():                                # create a function,
  try:
    l = [1, 5, 6, 7]                       # list
    i = int(input("Enter the index: "))    # akhanea data pustas kora hochea, input 0 to 3, because lista 4 ta datai achea.
    print(l[i])
    return 1
  except:                                  # 1st condition error holea "except" run hobea,
    print("Some error occurred")
    return 0

  finally:                                  # "finally" All-time executed hobea,
    print("I am always executed")

  print("I am always executed")             # all time executed this because ayta condition ar bairea run hochea, but Under in infection


x = func1()                                 # ""func1()"" "return" ar mun print koray,
print(x)





# "finally" ar kaj hochea, amra kuno kaj korchi, amra kuno program a koj korchi ta close kortea chachi, tokhon "finally" kea babohar kora hoy,
# full details janar jonno aro video dektea hobea,,, ""finally"" topic ar upor,

#   ""print(x)"" ar madhomea, "return" ar man print hoyea thakea,
