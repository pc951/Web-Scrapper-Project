import json
import math
import pathlib
from nltk import word_tokenize
from nltk.corpus import stopwords


def important_terms(document):
    tfidf = []
    for i, tokens in enumerate(document):
        scores = {word: tfidf(word, tokens, document) for word in tokens.words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        tfidf.append(sorted_words)

    # Top 40 words
    print(sorted_words[:40])

    # Top 10 terms
    term_list = []
    for ix, term in enumerate(sorted_words):
        important = term[0]
        if ix < 10:
            term_list.append(important)
    print(term_list)
    return term_list


# calculate tf
def tf(word, tokens):
    return tokens.words.count(word) / len(tokens.words)


def return_words(word, tokens):
    return sum(1 for tokens in tokens if word in tokens.words)


# calculate idf
def idf(word, tokens):
    return math.log(len(tokens) / (1 + return_words(word, tokens)))


# calculate tf-idf
def tf_idf(word, tokens):
    return tf(word, tokens) * idf(word, tokens)


def preprocess():
    # Preprocessing data
    # Tokenize the text, lower the case, etc
    new_text = movie_rating.split()
    print(new_text)
    tokens = word_tokenize(movie_rating)
    print(tokens)
    tokens = [t.lower() for t in tokens]
    print(tokens)
    tokens = [t for t in tokens if t.isalpha() and
              t not in stopwords.words('english')]
    return tokens


def knowledge_base():
    knowledge_file_data = open("knowledge_file_data.txt", "w")
    knowledge_file_data.close().write(knowledge_file_data)
    knowledge_file_data.close()
    return knowledge_file_data


if __name__ == "__main__":
    # Reading the file created from Web Scrapping
    text = open('IMDB Movie Ratings.txt', 'r')
    movie_rating = text.read()
    print(movie_rating)
    documents = preprocess()
    important_terms = important_terms()
    knowledge_base = knowledge_base()

