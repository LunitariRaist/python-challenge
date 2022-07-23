import pickle
import urllib.request

with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p') as response:
   html = response
answer = pickle.load(html)

print(answer)