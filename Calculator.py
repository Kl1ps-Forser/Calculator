class Fraction:
    def __init__(self, numer, denomir):
        self.numer = numer
        self.denomir = denomir

    def frac(self):
        print(self.numer/self.denomir)

class Arithmetic_operation:
    def __init__(self, f_num, s_num, sign):
        self.f_num = f_num
        self.s_num = s_num
        self.sign = sign


    def mathematical_exaple(self):
        if self.sign == "*":
            print(self.f_num * self.s_num)
        if self.sign == "+":
            print(self.f_num + self.s_num)
        if self.sign == "-":
            print(self.f_num - self.s_num)



class Temperature_conversion:
    def __init__(self, num_temp, temp):
        self.num_temp = num_temp
        self.temp = temp

    def tempcorv(self):
        if self.temp == "C" or self.temp == "c":
             print(str((self.num_temp * 1.8) + 32) + ' F')
        if self.temp == "F" or self.temp == "f":
             print(str((self.num_temp - 32) / 1.8) + ' C')


class Translation_of_mathematical_system:
    def __init__(self, num_ms, ms):
        self.num_ms = num_ms
        self.ms = ms

    def mscorv(self):
        if self.ms == 'miles' or self.ms == 'Miles':
            print(str(self.num_ms / 0.621371) + ' kilometers')
        if self.ms == 'miles' or self.ms == 'kilometers':
            print(str(self.num_ms * 0.621371) + ' miles')
        if self.ms == 'Liters' or self.ms == 'liters':
            print(str(self.num_ms / 3.785412) + ' halons')
        if self.ms == 'Halons' or self.ms == 'halons':
            print(str(self.num_ms * 3.785412) + ' liters')

move = str(input('Выберите действие Frac(деление), AO(арифметические операции), TC(перевод температур), TOFS(перевод из одной СИ в другую) - '))
if move == 'Frac':
    Fr = Fraction(int(input('Введите числитель - ')),int(input('Введите знаменатель - ')))
    Fr.frac()
if move == 'AO':
    AO = Arithmetic_operation(int(input('Введите первое число - ')),int(input('Введите второе число - ')), str(input('Введите знак - ')))
    AO.mathematical_exaple()
if move == 'TC':
    TC = Temperature_conversion(int(input("Введите кол-во градусов - ")), str(input('Введите f(F) или c(C) - ')))
    TC.tempcorv()
if move == 'TOFS':
    TOFS = Translation_of_mathematical_system(int(input("Введите кол-во миль/километров/галонов/литров - ")), str(input('Введите miles/kilometers/halons/liters - ')))
    TOFS.mscorv()
