a = ['1', '11', '21', '1211', '111221']

#      1 one 1 = 11
#     11 two 1s = 21
#     21 one 2 one 1 = 1211
#    1211 one 1 one 2 two 1s = 111221
#   111221 = three 1s two 2s one 1 = 312211
#  312211 = one 3 one 1 two 2s two 1s = 13112211



def sequencer(string):
    output = ''
    counter = 1
    if len(string) == 1:
        return f'1{string[0]}'
    for i in range(1, len(string)):
        if i < len(string) - 1:
            if string[i] == string[i-1]:
                counter += 1
            else:
                output += f'{counter}{string[i-1]}'
                counter = 1
        else:
            if string[i] == string[i-1]:
                counter += 1
                output += f'{counter}{string[i]}'
                return output
            else:
                output += f'{counter}{string[i-1]}'
                counter = 1
                output += f'{counter}{string[i]}'
                return output

num = '1'
for i in range(0, 31):
    print(len(num))
    num = sequencer(num)

    # answer: 5808