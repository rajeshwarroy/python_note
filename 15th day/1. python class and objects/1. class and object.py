class person:                  # class banaitea hoy "class" key word ar madhomea.
    name = 'Rajeshwar'
    occupation = 'Software Developer'
    networth = 10


    # 'self' hochea oy object, jar jonno method call kora hochea,
    def info(self):                 # method banailea 'self' keyword use korteai hobea,
        print(f'{self.name} is a {self.occupation}')

a = person()                                # "a" hochea akta object
b = person()                                # "b" hochea akta object
c = person()


a.name = 'Roni'                             # name kea change kora hochea.
a.occupation = 'Accountant'                 # occoupation kea change kora hochea.

b.name = 'Roy'                              # name kea change kora hochea.
b.occupation = 'Teacher'                    # occoupation kea change kora hochea.


print(a.name, a.occupation)
print('\n')
a.info()                                    # agea 'self' run hobea, then class ar madhomea object a asbea, object jea name a achea ta diyea run hobea, object ar porea data chenge hoyeachea tai new data use hobea and print hobea,
b.info()                                    # 'self' method run hobea, jeaheatu data change hoyeachea, tai new data output hobea,
c.info()                                    # Default data print
