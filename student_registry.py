
### methods below, still havent been added to the code:
# __str__ = "Student 1: Name: Francisco, Age: 15, Grade: 12th"
#advance "Francisco had advanced to the 13th grade"
#Study - "Francisco is studying Computer Science"

class Student:
    def __init__(self, name, age = 13, grade = "12"):
        self._name = name
        self._age = age
        self._grade = grade

    @property
    def get_name(self):
        return self._name
    
    @property
    def get_age(self):
        return self._age
    
    @property
    def get_grade(self):
        return self._grade

    @get_name.setter
    def set_name(self, new_name):
        if new_name.isalpha() and len(new_name) >= 3:
            self._name = new_name.title()
        else:
            print("Name must be only letters and at least 3 letters long")

    @get_age.setter
    def set_age(self, new_age):
        if  type(new_age) == int and new_age > 11 and new_age < 18:            
            self._age = new_age
        else:
            print("Age must be a number between 12 and 17")

    @get_grade.setter
    def set_grade(self, new_grade):
        if new_grade == "9th" or new_grade == "10th" or new_grade == "11th" or new_grade == "12th":
                self._grade = new_grade
        else:
            print("Please enter a grede between 9th and 12th grade, dont forget the th")


student1 = Student("John", 15, "10th")
print(student1.get_name)
print(student1.get_age)
print(student1.get_grade)

student1.set_name = "Batman"
student1.set_age = 16
student1.set_grade = "9th"
print(student1.get_name)
print(student1.get_age)
print(student1.get_grade)

student2 = Student("Robin")
print(student2.get_name)
print(student2.get_age)
print(student2.get_grade)