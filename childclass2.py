from my_package.module1 import Masters

class Major:
    def __init__(self, name, dept_name, joining_year):
        self.name = name
        self.dept_name = dept_name
        self.joining_year = joining_year
        
    def intro(self):
        return f"Myself {self.name} majoring in {self.dept_name} from {self.joining_year}."
    


