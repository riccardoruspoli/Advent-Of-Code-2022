# part 1
duplicate_items = []

with open('input.txt', 'r') as f:
    for line in f:
        line = line.replace('\n', '')
        first_compartment, second_compartment = line[:len(line) // 2], line[len(line) // 2 :]

        items = dict()
        for item in first_compartment:
            items[item] = True

        for item in second_compartment:
            if items.get(item):
                duplicate_items.append(item)
                break

# convert letter to priority
priority = 0
for item in duplicate_items:
    char = ord(item)
    if char >= 65 and char <= 90:
        priority += char - 38
    elif char >= 97 and char <= 122:
        priority += char - 96

print(priority)

# part 2
duplicate_items = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    while len(lines) > 0:
        line1, line2, line3 = lines.pop().replace('\n', ''), lines.pop().replace('\n', ''), lines.pop().replace('\n', '')

        dict1 = dict()
        dict2 = dict()
        dict3 = dict()

        for item in line1:
            dict1[item] = True

        for item in line2:
            if dict1.get(item):
                dict2[item] = True

        for item in line3:
            if dict2.get(item):
                dict3[item] = True
        
        duplicate_items.extend(dict3.keys())

print(duplicate_items)

# convert letter to priority
priority = 0
for item in duplicate_items:
    char = ord(item)
    if char >= 65 and char <= 90:
        priority += char - 38
    elif char >= 97 and char <= 122:
        priority += char - 96

print(priority)