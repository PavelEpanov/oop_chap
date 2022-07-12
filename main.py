class Employee:
    def computeSalary(self):
        pass
    def giveRaise(self):
        pass
    def promote(self):
        pass
    def retire(self):
        pass

# Тк класс инженер находится в древе ниже, чем класс работник, класс инженер переисполнит метод computeSalary
# Новый объект класса инженер будет ссылать на метод не класса РАБОТНИК, а класса ИНЖЕНЕР
class Engineer(Employee):
    def computeSalary(self):
        pass # Рассчитать зарплату как - нибудь по - другому

bob = Employee() # Стандартное поведение
alina = Engineer() # Специальный расчет заработной платы
pavel = Employee()

company = [bob, alina, pavel] # Составной объект

for emp in company: # Выполнить версию для данного объекта
    print(emp.computeSalary()) # Стандартную или специальную

