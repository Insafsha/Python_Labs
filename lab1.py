# 1. ФЛАГ литвы

print('#1')
red = '\x1b[48;5;196m'
yellow = '\x1b[48;5;220m'
green = '\x1b[48;5;82m'
stop = '\x1b[0m'
len = 40

def draw_line(color):
    line = ' ' * len
    print(color, line, stop, end='\n')

def flag_maker():
    for i in range(6):
        draw_line(yellow)
    for i in range(6):
        draw_line(green)
    for i in range(6):
        draw_line(red)
flag_maker()

#================================================================================================


# # # 2. График функции y = модуль(x)

white = '\x1b[48;5;15m'
stop = '\x1b[0m'
print()
print()
print()
print()
print('#2 график')
def draw_pix(start):
    print((start*3) + (white),' ', stop)

w = 10

def graph():
    for i in range(16, 8, -1):
        draw_pix(' '*i)
def graph2(w):
    for i in range(0, w-1):
        draw_pix(' '*i)

graph()
print('\u001b[10C]')
print('\u001b[10A]')
graph2(w)


print(' \n \n \n \n ')


# =============================================================================================================================


white = '\x1b[48;5;15m'
stop = '\x1b[0m'

def figure():
    j = 0
    k = 55
    for i in range(10, 1, -1):
        print(' ' * j, white + ' ' * (i + 1),  stop, ' ' * (k * 2 - i * 2) , white + ' ' *(i + 1), stop)
        j += i
        k -= i
    print(' ' * 55,  white + ' ' * 5, stop)
    print(' ' * 57,  white + ' ', stop)


figure()


# =============================================================================================================================



# Запустить отдельно



white = '\x1b[48;5;15m'
stop = '\033[0m'
file = open("sequence.txt")
file_ms = [abs(float(i)) for i in file]
nechet = [x for i, x in enumerate(file_ms) if i % 2 == 1]
chet = [x for i, x in enumerate(file_ms) if i % 2 == 0]

nechet_sum = sum(nechet)
chet_sum = sum(chet)

nechet_abs = nechet_sum / len(nechet)
chet_abs = chet_sum / len(chet)
common_nums_abs = sum(file_ms) / len(file_ms)

nechet_label = nechet_abs / common_nums_abs
chet_label = chet_abs / common_nums_abs

def draw_line(count):
    print(' ' * 10, white*(count < chet_label * 10), '  ', stop, ' ' * 20, white * (count < nechet_label* 10), '  ', stop,)

def chart():
    for i in range(max(int(chet_label) * 10, int(nechet_label) * 10), 0, -1):
        draw_line(i)
chart()
print(f"Четные числа: {chet_label}     Нечетные числа: {nechet_label}")

