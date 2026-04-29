class Book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.authot = author
        self.pages = pages
        self.year = year

    
    def title(self):
        return self._title  

    def author(self):
        return self._author

    def pages(self):
        return self._pages

    def year(self):
        return self._year



    def title(self, value):
        self._title = value

    def author(self, value):
        self._author = value

    def pages(self, value):
        self._pages = value

    def year(self, value):
        self._year = value
#######################################################


    def get_age(self):   #возраст книги
        return datetime.now().year - self._year


    def is_old(self):   #проверяет старше ли 20 лет
         return self.get_age() > 20


    def count_pages_per_year(self):    #страницы деленные на возраст 
        age = self.get_age()
        return self._pages / age 


