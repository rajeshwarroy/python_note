a = int(input("Enter any value between 5 and 9"))

if(a<5  or a>9):
  raise  ValueError("Value should be between 5 and 9")

#this is a kind of error, becouse Not Declare Full Condition,,,   Declare Only half Condition






#    new Defining Custom Exceptions

# class CustomError(Exception):
#     #code....
#     pass
#
# try:
#     #code....
#
# except CustomError:
#     #code
