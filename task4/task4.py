from sys import argv
import math

file_path = argv[1]

total_sum = 0
number_count = 0
total_deviation = 0

with open(file_path, encoding='utf-8') as file:
    data = file.read()
numbers = data.split('\n')
for number in numbers:
    number_count += 1
    total_sum += int(number)

average = round(total_sum / number_count)
for number in numbers:
    total_deviation += abs(average - int(number))

print(total_deviation)
