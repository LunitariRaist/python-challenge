import zipfile

def open_files():
    nothing = 'pychallenge6/90052.txt'
    i = 0
    while i < 909:
        with open(nothing, 'r') as f:
            text = f.read()
            print(text)
            f.close()
        nothing = 'pychallenge6/'
        for c in text:
            if c.isdigit():
                nothing += c
        nothing += '.txt'
        i += 1
    f.close()
    

# open_files()


# 46145.txt - collect the comments

with zipfile.ZipFile('channel.zip', 'r') as pyzip:
    output = ''
    for i in pyzip.infolist():
        for c in str(i.comment):
            if c.isalpha() and c.isupper() and c not in output:
                output += c
    print(output)

# EYONGX = OXYGEN