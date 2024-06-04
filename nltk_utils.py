import numpy as np
import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    """
        văn bản ban đầu => mảng chứa các từng chữ
    """
    return nltk.word_tokenize(sentence)


def stem(word):
    """
        giúp giảm các biến thể của từ về một từ gốc
        ví dụ:
        words = ["organize", "organizes", "organizing"]
        words = [stem(w) for w in words]
        -> ["organ", "organ", "organ"]
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    """
    chuyển đổi văn bản thành một tập hợp các từ về tần suất xuất hiện của các từ đó trong văn bản để xây dựng mô hình.
    ví dụ:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag