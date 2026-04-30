class University: 
	def __init__(self,name,founded_year,students_count,departments)

	self.name = name
	self.founded_year = founded_year
	self.students_count = students_count
	self.departments = departments

#getters
	def name(self):
		return self.name
	def founded_year(self):
		return self.founded_year
	def students_count(self):
		return self.students_count
	def departments(self):
		return self.departments

	def add_department(self,dept) #сыро
		dept = self.departments.append
		return {dept} 

#setters





#methods
	
	def __str__(self):
		return

	def get_age(self,founded_year):
	age = "Абстрактный календарь" - self.founded_year
	return age

	def get_info(self,name,founded_year,students_count):
		return (f "Название университета:{self.name}. Основан в {self.founded_year}. Кол.во учащихся:{self.students_count}")
		

	def list_departments(self, departments):
		for departments in self.departments
		print print (f "Факультеты: {dept}")
		return list_departments
	
	def get_ranking(self):
		return "Рейтинга нет" 
	
	def __getitem__(self,index):
		return self.department[index]

class TechicalUniversity(University):
	def __init__(self,name,founded_year,students_count,departments,specializations,ranking,teaching_age)
		super().__init__(name,founded_year,students_count,departments,specializations,ranking)
	self.ranking = ranking
	self.name = name
	self.founded_year = founded_year
	self.students_count = students_count
	self.departments = departments
	self.specializations = specializations
	self.teaching_age = teaching_age

#getters
	def name(self):
		return self.name
	def founded_year(self):
		return self.founded_year
	def students_count(self):
		return self.students_count
	def departments(self):
		return self.departments

	def specs(self,specializations)
		retrun self.specializations

	
	def get_age(self,teaching_age):
		return ("Стаж преподователя {self.teaching_age}") 
	

	def get_age(self,founded_year):
	age = "Абстрактный календарь" - self.founded_year
	return age

	def get_info(self,name,founded_year,students_count):
		return (f "Название университета:{self.name}. Основан в {self.founded_year}. Кол.во учащихся:{self.students_count}")
		

	def list_departments(self, departments):
		for departments in self.departments
		print print (f "Факультеты: {dept}")
		return list_departments
	
	def get_ranking(self):
		return (f Рейтинг университета {self.ranking}) 
	
	def __getitem__(self,index):
		return self.department[index]

	def __contains__(self,dept):
		for dept in self.
	
	
		