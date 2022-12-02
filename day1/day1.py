# part 1
max_calories = 0

with open('input.txt', 'r') as f:
    temp_calories = 0
    for line in f:
        if line == '\n':
            if temp_calories > max_calories:
                max_calories = temp_calories
            temp_calories = 0
        else:
            temp_calories += int(line)

print(max_calories)

# part 2
max_1 = 0
max_2 = 0
max_3 = 0

with open('input.txt', 'r') as f:
    temp_calories = 0
    for line in f:
        if line == '\n':
            if temp_calories > max_1:
                max_3 = max_2
                max_2 = max_1
                max_1 = temp_calories
            elif temp_calories > max_2:
                max_3 = max_2
                max_2 = temp_calories
            elif temp_calories > max_3:
                max_3 = temp_calories
            temp_calories = 0
        else:
            temp_calories += int(line)

print(max_1, max_2, max_3)
print(max_1 + max_2 + max_3)