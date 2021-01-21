import requests
import numpy as np

trump = requests.get('https://raw.githubusercontent.com/ryanmcdermott/trump-speeches/master/speeches.txt')
text = trump.text.lower()
words = text.split()
words = words[1:]

markov_dict = {}

for i,word in enumerate(words[:-1]):
    markov_dict[words[i]] = words[i+1]

first_word = np.random.choice(words)
chain = [first_word]
num_words = 100

for i in range(num_words):
    chain.append(markov_dict[words[np.random.choice(1000)]])

speech = ' '.join(chain)
print(speech)