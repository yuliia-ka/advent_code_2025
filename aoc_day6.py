########################################################
import math

########################################################
with open("C:\\Users\\ykazmin\\Desktop\\puzzle_input_day6_ex.txt", "r") as pup:
    input = pup.readlines()

collection_all = []

for a in range(len(input)):
    if a != len(input)-1:
        collection_all.append([int(b) for b in input[a].split()])
    else:
        collection_all.append(input[a].split())

operators = collection_all[-1]
input_rows = collection_all[:-1]

summing = 0

for col in range(len(operators)):
    print(col)
    numbers_collected = []
    for row in input_rows:
        print(row)
        numbers_collected.append(row[col])    
    if operators[col] == "*":
        summing += math.prod(numbers_collected)
    else:
        summing += sum(numbers_collected)

print("Part 1: ",summing)

############################
########## Part 2 ##########
############################

def column_widths(s):
    widths = []
    i = 0
    n = len(s)

    while i < n:
        if s[i] != " ":
            j = i + 1
            while j < n and s[j] == " ":
                j += 1
            widths.append(j - i)  # symbol + trailing spaces
            i = j
        else:
            i += 1

    return widths

def chunk_by_widths(seq, widths):
    out = []
    i = 0
    for w in widths:
        out.append(seq[i:i+w])
        i += w
    return out

with open("C:\\Users\\ykazmin\\Desktop\\puzzle_input_day6.txt", "r") as pup:
    input = pup.readlines()

input_rows = [s.rstrip('\n') for s in input]

operators = input[-1]
wide_list = column_widths(operators)
operators = operators.split()

input_rows = input[:-1]
input_rows = [chunk_by_widths(i,wide_list) for i in input_rows]
input_rows = [[a.replace(' ','0') for a in line] for line in input_rows]

summing = 0

for col in range(len(operators)):
    numbers_collected = []

    for digit in range(wide_list[col]):    
        one_vertical_number = ''
        
        for row in input_rows: 
            if row[col][digit]!='0':
                one_vertical_number += str(row[col][digit]).strip()

        if one_vertical_number != '':
            numbers_collected.append(int(one_vertical_number))

    if operators[col] == "*":
        summing += math.prod(numbers_collected)
    else:
        summing += sum(numbers_collected)

print("Part 2: ",summing)

########################################################