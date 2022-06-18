import tensorflow.keras

from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import InputLayer
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import TimeDistributed

from tensorflow.keras.optimizers import Adam

from tensorflow.keras.utils import to_categorical

import numpy as np
import nltk
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt
import random

from tqdm.notebook import tqdm as log_progress


def run(sentence):
    SEQUENCE_LENGTH = 17
    #converting the text into numbers to be processed by the embedding layer of the model
    words = [] #one of each word in tokenized will be in here
    filtering = lambda x : not x in words #for finding if the word should be added to the words array
    find = lambda x : float(words.index(x)) if x in words else float(len(words)) #convert each word into a number. -1 means that the item isn't in the vocabulary
    normalize = lambda x: [find(i)/len(words) for i in x]

    #test model
    sample_length = 200
    model = load_model("shakespear2.0.h5")

    words = []
    np_words = np.load(open('words.npy', 'rb'))
    words = np_words.tolist()
        
    #get input sentence and process
   # sentence = input("Enter first " + str(SEQUENCE_LENGTH) + " letters... ").lower()

    def process(data):
        output = normalize([data])
        output = np.asarray(output, np.float32)
        output = np.reshape(output, (output.shape[0], 1, SEQUENCE_LENGTH))
        return output

    tokenized = [item for item in sentence]
    root = []
    if len(tokenized) <= SEQUENCE_LENGTH:
        print("Input text isn't long enough!")
        while True:
            pass
        
    for i in range(int(len(tokenized) - SEQUENCE_LENGTH)):
        root.append(normalize(tokenized[i:i+SEQUENCE_LENGTH]))
    root = np.asarray(root, np.float32)
    root = np.reshape(root, (root.shape[0], SEQUENCE_LENGTH, 1))

    last_input = root[root.shape[0]-1]

    output = sentence
    pred = model.predict(root, verbose=0)
    sequence = sentence[len(output)-SEQUENCE_LENGTH-2:len(output)-1]

    for i in log_progress(range(sample_length)):
        tokenized = [item for item in sequence]
        
        root = []
        for i in range(int(len(tokenized) - SEQUENCE_LENGTH)):
            root.append(normalize(tokenized[i:i+SEQUENCE_LENGTH]))
        root = np.asarray(root, np.float32)
        root = np.reshape(root, (root.shape[0], SEQUENCE_LENGTH, 1))
        
        tmp = root[root.shape[0]-1]
        tmp = np.reshape(tmp, (1, SEQUENCE_LENGTH, 1))
        
        
        pred = model.predict(tmp, verbose=0)
        #output += words[np.random.choice(len(pred[pred.shape[0]-1]), p=pred[pred.shape[0]-1])]
        sequence = sequence[1:]
        sequence += words[pred.argmax()]
        output += words[pred.argmax()]

    return output