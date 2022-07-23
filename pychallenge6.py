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
    

open_files()

# collect the comments

