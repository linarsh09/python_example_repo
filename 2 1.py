#вариант 10
class University:
    def __init__(self, name, founded_year, students_count):
        self.name = name
        self.founded_year = founded_year
        self.students_count = students_count
        self.departments = []

    def add_department(self, dept):
        self.departments.append(dept)

    def get_age(self):
        age = 2026 - self.founded_year
        return age

    def get_info(self):
        return self.name + " " + str(self.founded_year)

    def list_departments(self):
        for d in self.departments:
            print(d)

    def get_ranking(self):
        return "normal"


class TechnicalUniversity(University):
    def __init__(self, name, founded_year, students_count):
        University.__init__(self, name, founded_year, students_count)
        self.specializations = []

    def add_specialization(self, spec):
        self.specializations.append(spec)

    def get_age(self):
        age = 2026 - self.founded_year - 2
        return age

    def get_ranking(self):
        return "high"

    def list_departments(self):
        print("technical:")
        for d in self.departments:
            print(d)


u = University("KSTU", 2001, 5000)

u.add_department("IT")
u.add_department("Math")

u.list_departments()

print(u.get_age())
print(u.get_info())



