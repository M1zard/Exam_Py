import math
# 1
summ = 0
a = int(input())
for i in range(1,a+1):
    summ+=i
print(summ)

#2
for i in range(1,10+1):
    print(f"3*{i} = {3*i}")

#3
N = int(input())
Num = 0
while N > 0:
    Num +=1
    print(Num ** 2)
    N -= 1

#4
num = 0
while True:
    a = int(input())
    if a != 0:
        num+= a
    else:
        print("Число равняется 0")
        break

#5
listochek = [1,2,3,4,5,6,7,8,9,10]
print(sum(listochek))

#6
listok =[1,-2,3,4,5,-6,7,8,-9,10]
Minus = 0
Plus = 0
for i in listok:
    if i >= 1:
        Plus+=1
    else:
        Minus+=1

print(f"Плюсовые: {Plus} Минусовые: {Minus}")

#7
def arip(list):
    return print(f"Сумма: {sum(list)} Среднее Арифмитическое: {sum(list) / len(list)}")
arip([1,2,3,4,5])

#8
def area(figure,length):
    match figure:
        case "Square":
            return f"Площадь квадрата {length**2}"
        case "Triangle":
            return f"Площадь треугольника {length**2 * math.sqrt(3) / 4}"
        case "Circle":
            print("1-Выберите если ввели в радиусе \n 2-Если в диаметре")
            a = int(input())
            if a == 1:
                return f"Площадь круга {math.pi * (length ** 2)}"
            if a == 2:
                return f"Площадь круга {math.pi * (lenght ** 2) / 4}"
        case _:
            print("Неверный выбор!")
print(area("Circle",100))