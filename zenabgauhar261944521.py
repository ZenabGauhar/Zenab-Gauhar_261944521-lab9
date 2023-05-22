class Shape:
    def __init__(self, sides):
        self.sides = sides
    
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(3)
        self.base = base
        self.height = height
    
    def area(self):
        print (0.5 * self.base * self.height)
    

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(0)
        self.radius = radius
    
    def area(self):
        print( 3.174 * self.radius * self.radius)
        
def main():
    tri=Triangle(7,8)
    tri.area()
    cir=Circle(22)
    cir.area()
main()

#Q2
class Employee:
    def __init__(self, emp_name, emp_id, salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.salary = salary
    
    def salary_status(self):
        print( "Salary: Rs" ,self.salary)

class BM(Employee):
    def __init__(self, emp_name, emp_id):
        super().__init__(emp_name, emp_id, 10000)

class PM(Employee):
    def __init__(self, emp_name, emp_id):
        super().__init__(emp_name, emp_id, 12000)

class LM(Employee):
    def __init__(self, emp_name, emp_id):
        super().__init__(emp_name, emp_id, 15000)

def main():
    employees = [
        BM("abc", 1),
        PM("def", 2),
        LM("ghi", 3)
    ]

    for employee in employees:
        print("Employee Name:", employee.emp_name)
        print("Employee ID:", employee.emp_id)
        employee.salary_status()
        print()

main()
