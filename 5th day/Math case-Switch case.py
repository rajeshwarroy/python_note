x = int(input("Enput the value of x: "))
# x is the variable to match
match x:
    # if x is zero
    case 0:
        print("x id zero")
    # case with if-condition
    case 4:
        print("case is 4")
    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _ :                         # Default case ar jonno "" _ "" use kora hoy python a.
        print(x)


# kuno case match na hoylea default case match hobeai..     ayta ak porar 'else' ar moto kaj korea
# Break korar lagea na python a,, c, c++, java tea jeamon use korar lagea, python a lagea na.
    # case _ if x!=90:
    #     print(x, "is not 90")
    # case _ if x!=80:
    #     print(x, "is not 80")
