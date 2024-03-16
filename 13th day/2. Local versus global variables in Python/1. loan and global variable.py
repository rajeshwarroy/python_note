# amar kachea ak "Variable" achea ta amra ak "function" ar vitor banaichi, ta ki amra "function" ar bairea use kortea parbo?
# amra ayta use kortea parbo na. ay jonno ayta "local Variable" bolea.

# amar klachea akta "Variable" achea ta "function" ar bairea create kora hoyeachea, oy "Variable" kea amra function ar vitor ao use kortea parbo,
# "function" ar baireao use kortea parbo. ayjonno aytakea "global Variable" bolea.






x = 10  # global variable


def my_function():
  global x          # global variable kea niyea asa hoy "global scop" ar madhomea.
  x = 5             # this will change the value of the global variable x
  y = 5             # local variable


my_function()
print(x)            # prints 5      , because "function" ar vitorea "global scop x" ar man "x=5" korea dichi.
# print(y)            # this will cause an error because y is a local variable and is not accessible outside of the function
