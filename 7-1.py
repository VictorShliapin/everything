import RPi.GPIO as gpio
import time
from matplotlib import pyplot

gpio.setmode(gpio.BCM)
leds = [21, 20, 16, 12, 7, 8, 25, 24]
gpio.setup(leds, gpio.OUT)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
gpio.setup(dac, gpio.OUT, initial=gpio.HIGH)

comp = 4
troyka = 17
gpio.setup(comp, gpio.IN)


# Функция для снятия показаний с troyka-module
def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2**i
        gpio.output(dac, translate(k))
        time.sleep(0.005)
        if gpio.input(comp) == 0:
            k -= 2**i
    return k


# Функция перевода в двоичную систему счисления
def translate(a): return [int(elem) for elem in bin(a)[2:].zfill(8)]


# Функция создания графиков
def graphics(time_experiment, count, results_measured):
    print('Построение графиков...')
    y = [i / 256 * 3.3 for i in results_measured]
    x = [i * time_experiment / count for i in range(len(results_measured))]
    pyplot.plot(x, y)
    pyplot.xlabel('t(c)')
    pyplot.title('')
    pyplot.ylabel('V')
    pyplot.show()


try:
    napr = 0
    results_measured = []
    time_start = time.time()
    count = 0

    gpio.setup(troyka, gpio.OUT, initial=gpio.LOW)

    # Зарядка конденсатора, записываем показания в процессе
    print('Начало зарядки конденсатора...')
    while napr < 135:
        print(napr)
        napr = adc()
        results_measured.append(napr)
        time.sleep(0)
        count += 1
        gpio.output(leds, translate(napr))

    gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)

    # Разрядка конденсатора, записываем показания в процессе
    print('Начало разрядки конденсатора...')
    while napr > 250 * 0.02:
        print(napr)
        napr = adc()
        results_measured.append(napr)
        time.sleep(0)
        count += 1
        gpio.output(leds, translate(napr))

    time_experiment = time.time() - time_start

    # Запись данных в файлы
    print('Запись данных в файл...')
    with open('data.txt', 'w') as f:
        for i in results_measured:
            f.write(str(i) + '\n')
    with open('setings.txt', 'w') as f:
        f.write(str(1 / (time_experiment / count)) + '\n')
        f.write(f"{3.3 / 256}")

    print(f"Общая продолжительность эксперимента: {time_experiment}")
    print(f"Период одного измерения: {time_experiment / count}")
    print(f"Средняя частота дискретизации: {1 / time_experiment / count}")
    print('')
    print('')

    
    # Выводим графики
    graphics(time_experiment, count, results_measured)

finally:
    gpio.output(leds, 0)
    gpio.output(dac, 0)
    gpio.cleanup()
