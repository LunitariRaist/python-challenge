import urllib.request


# urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
# end. 400 times is more than enough.

# open url and read the response
# loop over the response to get a new url
# update the request to include the new url

def get_nothings():
    nothing = '12345'
    i = 0
    while i < 400:
        url = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}'
        with urllib.request.urlopen(url) as response:
            html = response.read()
        print(html)
        nothing = ''
        for c in html:
            if chr(c).isdigit():
                nothing += chr(c)
        i += 1
    

get_nothings()

# peak.html