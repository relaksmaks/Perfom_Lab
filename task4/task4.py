from sys import argv

numbers_path = argv[1]

sum = 0
count = 0
answer = 0

with open(numbers_path, encoding='utf-8') as numbers:
    data = numbers.read()
nums = data.split('\n')
for num in nums:
    count += 1
    sum += int(num)

mid = round(sum / count)
for num in nums:
    answer += abs(mid - int(num))

print(answer)