class students:
    no_of_std = 0
    def __init__(self, name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        students.no_of_std += 1
    def descripe(self):
        return f"hello {self.name} your age is {self.age} congrats on your salary ({self.salary})"

st1 = students("amr", 20, 5618)
st2 = students("anwar", 22, 5118)


print(st1.name, st1.age, st1.salary)
print(st2.name, st2.age, st2.salary)
print(students.no_of_std)
print(st1.descripe())



