# writing a file

f = open('myfilewriting.txt', 'w')          # file open kora hoy, ay name a file na thaklea create korea naoya hoy.
f.write('hello, world! ')                   # file a write kora hoy,
f.close()                                   # file close kora hoy.




f = open('myfilewriting.txt', 'a')          # file open kora hoy, ay name a file na thaklea create korea naoya hoy.
f.write("I'm Rajeshwar. ")                  # file a write kora hoy, agea kuno data thaklea oy datar porea sum hoyea thakea,
f.close()                                   # file close kora hoy.




with open('myfilewriting.txt', 'a') as f:   # "[open('myfilewriting.txt', 'a')]" kea "f" ar modhea rakhi.
    f.write("Hey I am inside with.")        # write kori.
