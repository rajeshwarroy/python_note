# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode



import string
import random
n=3
res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
st = input("Enter message")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding")
coding = True if (coding=="1") else False     # short coding use kora hoyeachea,; "coding==1" hoylea "if" cholbea, 1 badea onno kichu dilea  "false" cholbea,
print(coding)
if(coding):
  nwords = []               # "nwords = []" hochea amar "empty string"
  for word in words:        # for loop a words kea word a niyea nichi,
    if(len(word)>=3):       # if condition "word" ar length 3 ar basi hotea hobea,
      r1 = "dsf"            # "3 random code" in use korar jonno, akhanea apatoto "hard code" daoya achea,
      r2 = "jkr"            # "3 random code".
      # stnew = r1+ word[1:] + word[0] + r2     # "r1" & "r2" random Character,;    "word[1:]" sob character nibea, "word[0]" 1st character nibea,
      stnew = str(res)+ word[1:] + word[0]+str(res)    # "r1" & "r2" random Character,;    "word[1:]" sob character nibea, "word[0]" 1st character nibea,
      nwords.append(stnew)                    # ".append" aar kaj hochea "stnew" ar data "nwords" ar sathea add kora,
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))                     # The join() method takes all items in an iterable and joins them into one string.
                                              # A string must be specified as the separator.

else:
  nwords = []
  for word in words:
    if(len(word)>=3):                         # condition Check,
      stnew = word[3:-3]                      # " word[3:-3] " ar madhomea, "first 3 character" and "last 3 character" delete korbea agea,
      stnew = stnew[-1] + stnew[:-1]          # "stnew[-1]" ar madhomea last character delete korea, ta "stnew[:-1]" first a sum korea dibea,
      nwords.append(stnew)                    # "append(stnew)" kea "nwords" ar sathea add korea dibea.
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))


