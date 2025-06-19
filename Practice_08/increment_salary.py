class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def increment_salary(self, percentage):
        self.percentage = percentage
    
    def after_increment(self):
        print(f"Salary before increment: {self.salary}")
        self.salary += self.salary * (self.percentage / 100)
        print(f"Salary after increment: {self.salary}")


employee1 = employee("Desai Kunj", 50000)
employee1.increment_salary(10)  # Increment salary by 10%
employee1.after_increment()  # Update salary after increment
 

