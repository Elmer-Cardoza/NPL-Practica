import nltk
import urllib.request
import re
from inscriptis import get_text
from nltk import word_tokenize, sent_tokenize
from googletrans import Translator
#nltk.download()

#articulo de wikipedia
#enlace = "https://en.wikipedia.org/wiki/Gualaca_bus_crash"
#html = urllib.request.urlopen(enlace).read().decode('utf-8')
text = "On February 15, 2023, 39 people were killed in a bus crash in Panama. It was headed to a migrant reception center in the town of Gualaca when it crashed in Gualaca District, Chiriquí Province, in the west of the country about 67.8 km (42.1 mi) from the Costa Rican border."
article_text = text
article_text = text.replace("[ edit ]", "")
print ("###############################")
translator = Translator()

from nltk import word_tokenize, sent_tokenize
#Removing Square Brackets and Extra Spaces
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)

formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

#nltk.download()
#En esta parte hace la tokenizacion
sentence_list = nltk.sent_tokenize(article_text)

#En esta parte encuentra la frecuencia de las palabras
stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1

#Calcula las frases que mas se repiten
sentences_socores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 50:
                if sent not in sentences_socores.keys():
                    sentences_socores[sent] = word_frequencies[word]
                else:
                    sentences_socores[sent] += word_frequencies[word]

maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

#Realiza el resumen con las mejores frases
import heapq
summary_sentences = heapq.nlargest(7, sentences_socores, key=sentences_socores.get)
summary = ' '.join(summary_sentences)
traductor = Translator()

translated=traductor.translate(summary, dest='spanish')
print(translated.text)
from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()