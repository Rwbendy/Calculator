def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
        return "На 0 делить нельзя"
    return x / y

def integer_divide(x,y):
    if y == 0:
        return "На 0 делить нельзя"
    return x // y
def percentage(x,y):
    return x * 100 / y
def reciprocal(x):
    if x == 0:
        return "На 0 делить нельзя"
    return 1 / x
def square(x):
    return x ** 2

def square_root(x):
    return x ** 0.5


print("Выберите операцию")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Целочисленное деление")
print("6. Процент от числа")
print("7. 1 / x")
print("8. возведение в степень")
print("9 Квадратный корень")


while True:
    choice = input("Введите номер операции (1/2/3/4/5/6/7/8/9)")

    if choice in ("1","2","3","4","5","6"):
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введиет второе число: "))
        if choice == "1":
            print(F"{num1} + {num2} = {add(num1,num2)}")
        elif choice == "2":
            print(F"{num1} - {num2} = {subtract(num1,num2)})")
        elif choice == "3":
            print(F"{num1} * {num2} = {multiply(num1,num2)}")
        elif choice == "4":
            print(F"{num1} / {num2} = {divide(num1,num2)}")
        elif choice == "5":
            print(F"{num1} % {num2} = {percentage(num1,num2)}")
        elif choice == "6":
            print(F"{num1} // {num2} = {reciprocal(num1)}")
        next_calculation = input("Хотите сделать ещё один расчёт? (Да/Нет): ")
        if next_calculation in ("1", "2", "3", "4", "5", "6", "7", "8"):
            break
        else:
            print("Неверный ввод")

    if choice in ("7", "8", "9"):
        num3 = float(input(("Введите число")))
        if choice == "7":
            print(F"{1} / {num3} = {reciprocal(num3)}")
        elif choice == "8":
            print(F"{num3} ** {2} = {square(num3)}")
        elif choice == "9":
            print(F"{num3} ** {0.5} = {square_root(num3)}")


        next_calculation = input("Хотите сделать ещё один расчёт? (Да / Нет): ")
        if next_calculation in ("1","2","3","4","5","6","7","8","9"):
            break
        else:
            print("Неверный ввод")

