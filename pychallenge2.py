# find rare characters in pychallenge2.txt


def make_list_of_characters():
    char_list = []
    with open('pychallenge2.txt', 'r') as f:
        for c in f:
            char_list += c
    return char_list


char_list = make_list_of_characters()


def find_unique_characters():
    new_list = []
    for i in char_list:
        if i in new_list:
            pass
        else:
            new_list += i
    return new_list

print(find_unique_characters())

# ['%', '$', '@', '_', '^', '#', ')', '&', '!', '+', ']', '*', '}', '[', '(', '{', '\n', 
# 'e', 'q', 'u', 'a', 'l', 'i', 't', 'y']