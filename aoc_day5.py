with open("C:\\Users\\ykazmin\\Desktop\\puzzle_input_day5.txt", "r") as pup:
    input = pup.readlines()

where_split = input.index('\n')
ranges = input[:where_split]
searches = input[where_split+1:]


ranges = [a.replace('\n','') for a in ranges]
ranges = [tuple(map(int, a.split('-'))) for a in ranges]
#ranges = [a.split('-') for a in ranges]
#ranges = [[int(a[0]),int(a[1])] for a in ranges]

ranges.sort()
searches = [int(a.replace('\n','')) for a in searches]
searches.sort()
#print(ranges[0:])
#print(searches)

counter = 0
consider_list_from = 0

for i in searches:
    for r in ranges[consider_list_from:]:
        r_start = r[0]
        r_end = r[1]
        if (i>= r_start) & (i<=r_end):
            #print(i)
            counter += 1
            consider_list_from = ranges.index(r)
            break

print("Part 1: ", counter)

list_chad_len = 0
global_max_end = 0

for idx, r in enumerate(ranges):
    
    r_start = r[0]
    r_end = r[1]

    # if idx == 0:
    #     list_chad_len += r_end - r_start + 1
    #     global_max_end = r_end
        
    # if idx > 0:
    # if r_start == r_end: 
    #     if global_max_end > r_end:
    #         pass
    #     else:
    #         list_chad_len +=1
    #         global_max_end = r_end
    # else:
    r_start = max(r_start, global_max_end+1)
    r_end = max(r_end, global_max_end)  
    
    list_chad_len += r_end - r_start + 1
    global_max_end = r_end

print("Part 2: ",list_chad_len)