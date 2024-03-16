class Employee:
    name = "Rajeshwar"
    def __len__(self):
        i = 0
        for c in self.name:     # নাম এর ডাটার len কত আছে তা for লুপ  আর মাধমে গণনা করা হচ্ছে।
            i = i + 1
        return i
e = Employee()
print(e.name)
print(len(e))                   # len(e) এখানে len দেখবে 'e' এর ডাটার
