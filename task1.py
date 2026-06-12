class Employee:
    def __init__(self):
        self.__salary = 5000

        def increment(self):
            self.__salary = self.__salary + 1000

            def deduct(self):
                self.__salary = self.__salary - 5000

                def get_salary(self):
                    print("salary is:", self.__salary)

e1 = Employee()
e2 = Employee()

print("Employee 1")
e1.gets_salary()
e1.increment()
e2.get_salary()
e1.deduct()
e1.get_salary()

print("Employee 2")
e2.get_salary()
e2.increment()
e2.get_salary()
e2.deduct()
e2.get_salary()
