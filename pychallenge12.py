data = open("pychallenge12.gfx", "rb").read()
new_list = []
for i in range(0, 67575, 5):
    new_list.append(data[i])

print(len(new_list))

tuples_list = []
for i in range(0, 13515, 3):
    tuples_list.append((new_list[i], new_list[i+1], new_list[i+2]))

print(tuples_list)

# answer: 