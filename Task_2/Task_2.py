#  Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*
# 6 -> 1  4  1
#   24 -> 4  16  4
#    60 -> 10  40  10

s = int(input('Введите вообщем сколько сделано журавликов: '))
Seryzha_Peter  = s // 6
Katya = (s // 6) * 4
print(f'Сережа и Петя сделали журавликов = {Seryzha_Peter}, а Катя сделала = {Katya}')
