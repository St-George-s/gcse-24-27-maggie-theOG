heights = [2.4, 3.8, 0.4, 6.7]
names = ["benjamin franklin", "JJ bittenbinder", "elizabeth the third", "freddie mercury"] #start at 0

print(names[1])
print(heights[1])

for counter in range(len(names)):
    print(names[counter])
    print(heights[counter]) 

# append (add) to array

heights.append(67)
names.append("jerry")