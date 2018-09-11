from nltk.tokenize import sent_tokenize
#Enter any paragraph in text as ->text="my name is ...."
tokenized_text=sent_tokenize(text)
print(tokenized_text)

from nltk.tokenize import word_tokenize
tokenized_word=word_tokenize(text)
print(tokenized_word)

from nltk.probability import FreqDist
fdist = FreqDist(tokenized_word)
print(fdist)

fdist.most_common(2)

import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()

from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
print(stop_words)

filtered_sent=[]
for w in tokenized_text:
    if w not in stop_words:
        filtered_sent.append(w)
print("Tokenized Sentence:",tokenized_text)
print("Filterd Sentence:",filtered_sent)

from nltk.stem import PorterStemmer
ps=PorterStemmer()
tokenized_word_text=word_tokenize(text)
tokenized_sent_text=sent_tokenize(text)

stemmed_words=[]
for w in filtered_sent:
    stemmed_words.append(ps.stem(w))
print("Filtered sentence:",filtered_sent)
print("Stemmed sentence:",stemmed_words)

