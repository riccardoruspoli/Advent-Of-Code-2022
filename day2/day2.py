# part 1
total_score = 0

with open('input.txt', 'r') as f:
    for line in f:
        row = line.replace('\n', '').split(' ')
        e = row[0]
        p = row[1]

        if p == 'X':
            total_score += 1
        elif p == 'Y':
            total_score += 2
        elif p == 'Z':
            total_score += 3

        if (p == 'X' and e == 'C') or (p == 'Y' and e == 'A') or (p == 'Z' and e == 'B'):
            total_score += 6
        elif (p == 'X' and e == 'A') or (p == 'Y' and e == 'B') or (p == 'Z' and e == 'C'):
            total_score += 3

print(total_score)

# part 2
total_score = 0

with open('input.txt', 'r') as f:
    for line in f:
        row = line.replace('\n', '').split(' ')
        e = row[0]
        r = row[1]

        if r == 'X':
            if e == 'A':
                total_score += 3
            elif e == 'B':
                total_score += 1
            elif e == 'C':
                total_score += 2
        elif r == 'Y':
            total_score += 3
            if e == 'A':
                total_score += 1
            elif e == 'B':
                total_score += 2
            elif e == 'C':
                total_score += 3
        elif r == 'Z':
            total_score += 6
            if e == 'A':
                total_score += 2
            elif e == 'B':
                total_score += 3
            elif e == 'C':
                total_score += 1

print(total_score)