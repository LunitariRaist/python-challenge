def get_characters():
    char_list = []
    with open('pychallenge3.txt', 'r') as f:
        for c in f.read():
            char_list += c
    return char_list


char_list = get_characters()


def check_letters(l):
    answer = []
    for c in l:
        if c.islower():
            if len(answer) == 3:
                answer += c
            elif len(answer) == 7:
                print(answer)
                answer = []
            else:
                answer = []
        elif c.isupper():
            if answer == ['alert']:
                pass
            elif len(answer) < 3:
                answer += c
            elif len(answer) == 3:
                answer = ['alert']
            elif len(answer) < 7:
                answer += c
            else:
                answer = ['alert']

test_list = ['U', 'Z', 'G', 's', 'I', 'E', 'T', 'M', 'V', 'Z', 'B', 'a', 'R', 'Z', 'T', 'j', 'i', 'N', 'b', 'E', 'F', 'G', 'H', 'I', 'j', 'K', 'L', 'M', 'N', 'o', 'O', 'O', 'O', 'p', 'q', 'R', 's', 'T', 'U', 'v', 'W', 'a', 'X', 'X', 'X', 'x', 'X', 'X', 'X', 'y', 'z']

check_letters(char_list)
# check_letters_lax(test_list)