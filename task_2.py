# Задача №2. Петя и Катя – брат и сестра. Петя – студент, а Катя – 
#            школьница. Петя помогает Кате по математике. Он задумывает два 
#            натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для 
#            этого Петя делает две подсказки. Он называет сумму этих чисел S и 
#            их произведение P. Помогите Кате отгадать задуманные Петей числа.

s = int(input("Введите сумму загаданных чисел S: "))
p = int(input("Введите произведение загаданных чисел P: "))

x, y = 0, 0

for i in range(s):   
    x = s - i
    y = s - x     
    if x + y == s and x * y == p:
        break    
print(x, y)