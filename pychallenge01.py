crypto_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


def shift_characters_by_two(str):
    new_string = ''
    for c in str:
        if c in " .()'":
            new_string += c
        elif c == 'y':
            new_string += 'a'
        elif c == 'z':
            new_string += 'b'
        elif ord(c) in range(97, 121):
            new_string += chr(ord(c) + 2)

    return new_string

print(shift_characters_by_two(crypto_string))

url = 'map'

print(shift_characters_by_two(url))

# i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

# answer: ocr