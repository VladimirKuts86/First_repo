list_of_heights = [100, 110, 105, 120, 125, 130, 128]
current = []
longest = []
for i in range(len(list_of_heights)-1):
    if list_of_heights[i] < list_of_heights[i+1] and list_of_heights[i] < list_of_heights[i-1] and (i != 0):
        i = i+1
        continue
    elif list_of_heights[i] < list_of_heights[i+1]:
        current.append(list_of_heights[i])
    else:
        current.append(list_of_heights[i])
        if len(current) > len(longest):
            longest = current
            current = []
print(longest) 