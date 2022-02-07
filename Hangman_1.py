# write a function that picks a random word from a list of words from the SOWPODS dictionary.



import requests
import numpy as np

url = 'http://norvig.com/ngrams/sowpods.txt'
r = requests.get(url).text

# list with strings
l = r.split('\n') 

# to return a string
def pickword():
    return ''.join(np.random.choice(l, 1))

print(pickword())
