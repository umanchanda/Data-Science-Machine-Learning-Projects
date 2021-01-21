import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

# nltk.download('stopwords')
# nltk.download('punkt')
stop_words = set(stopwords.words('english'))
tokenizer = RegexpTokenizer(r'\w+')

def get_data(f):
    words = []

    with open(f) as file:
        soup = BeautifulSoup(file, 'html.parser')
        a_tags = soup.find_all('a')
        for a in a_tags:
            sentence = tokenizer.tokenize(a.contents[0].lower())
            for word in sentence:
                if word not in stop_words and word != 'area':
                    words.append(word)
    return words

def plot_data(top_20):
    words = [x[0] for x in top_20]
    counts = [x[1] for x in top_20]
    x_pos = np.arange(len(words))

    plt.figure(figsize=(12,8))
    plt.bar(x_pos, counts, align='center')
    plt.xticks(x_pos, words, rotation=30)
    plt.xlabel('Words')
    plt.ylabel('Frequencies')
    plt.show()

def main():
    f = 'MyActivity.html'
    words = get_data(f)
    word_counter = Counter(words)
    top_20 = word_counter.most_common(20)
    plot_data(top_20)


if __name__ == "__main__":
    main()
