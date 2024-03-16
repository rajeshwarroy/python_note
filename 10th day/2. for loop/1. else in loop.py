for i in range(6):      # range joto dibo toto porjonto run hoeba. 0 to start and range ar porjonto (range-1)
    print(i)            # print "i", and last tea "else" run hobea

else:                       # else print hobai jai thakun na kano,, last a
    print("Sorry no i")




print('\n')
for i in range(6):      # range joto dibo toto porjonto run hoeba. 0 to start and range ar porjonto (range-1)
    print(i)            #
    if i == 3:          # i == 3 condition cheack korbea.
    # if i == 6:         # i == 6 joylea, program 6 porjonto run hobea , taholea Condition false hobea
        break           # condition true hoylea break hobea. and for loop stop/ber hoyea jabea
else:                       #
    print("Sorry no i")
print('\n')






#   for loop program.
for x in range(5):
    print("iteration no {} in for loop".format(x+1))   # ".format(x+1)" ar madhomea ""{}"" a range ar number ta bosteachea.
else:                                               #(x+1) manea fist a "0+1=1"vkorteachea, fust number 1 hobea taholea.
    print("else block in loop")
print("Out of loop")
