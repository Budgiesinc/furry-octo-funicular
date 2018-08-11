# things we need for NLP
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

# things we need for Tensorflow
import numpy as np
import tflearn
import tensorflow as tf
import random

# import our chat-bot intents file
import json
with open('intents.json') as json_data:
    intents = json.load(json_data)

#
#
#
#
#
#
#
#
#
words = []
classes = []
documents = []
ignore_words = ['?']


# loop through each sentence in our intents patterns
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # tokenize each word in the sentence
        w = nltk.word_tokenize(pattern)
        # add to our words list
        words.extend(w)
        # add to documents in our corpus
        documents.append((w, intent['tag']))
        # add to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# stem and lower each word and remove duplicates
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

# remove duplicates
classes = sorted(list(set(classes)))

print (len(documents), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique stemmed words", words)

# 27 documents
# 9 classes ['goodbye', 'greeting', 'hours', 'mopeds', 'opentoday',
# 'payments', 'rental', 'thanks', 'today']
# 48 unique stemmed words ["'d", "'s", 'a', 'acceiv', 'anyon', 'ar', 'bye',
# 'can', 'card', 'cash', 'credit', 'day', 'do', 'doe', 'good', 'goodby', 'hav',
# 'hello', 'help', 'hi', 'hour', 'how', 'i', 'is', 'kind', 'lat', 'lik', 'mastercard',
# 'mop', 'of', 'on', 'op', 'rent', 'see', 'tak', 'thank', 'that', 'ther', 'thi', 'to', 'today',
# 'we', 'what', 'when', 'which', 'work', 'yo', 'you']


#
#
#
# create our training data
training = []
output = []
# create an empty array for our output
output_empty = [0] * len(classes)

# training set, bag of words for each sentence
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # stem each word
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    # create our bag of words array
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training)

# create train and test lists
train_x = list(training[:,0])
train_y = list(training[:,1])

#
#
#

# reset underlying graph data
tf.reset_default_graph()
# Build neural network
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
# Start training (apply gradient descent algorithm)
model.fit(train_x, train_y, n_epoch=1000, batch_size=8, show_metric=True)
model.save('model.tflearn')

#
# Training Step: 3999  | total loss: 0.54986 | time: 0.008s
# | Adam | epoch: 1000 | loss: 0.54986 - acc: 0.9616 -- iter: 24/27
# Training Step: 4000  | total loss: 0.50465 | time: 0.011s
# | Adam | epoch: 1000 | loss: 0.50465 - acc: 0.9654 -- iter: 27/27
# --
# INFO:tensorflow:/home/gk/gensim/notebooks/model.tflearn is not in
# all_model_checkpoint_paths. Manually adding it.
#
#
def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))

#
#
#
#
#

p = bow("is your shop open today?", words)
print (p)
print (classes)
#
#
# [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0
#  0 0 0 1 0 0 0 0 0 1 0]
# ['goodbye', 'greeting', 'hours', 'mopeds', 'opentoday', 'payments', 'rental',
# 'thanks', 'today']

#
#
#
#
#

print(model.predict([p]))

#
# [[5.111963474746517e-08, 0.00029038049979135394, 0.19395901262760162,
# 4.018096966262874e-10, 0.7987914085388184, 0.0005724101793020964,
# 8.153344310812827e-08, 5.96670907127006e-11, 0.0063865589909255505]]

#
#

# save all of our data structures
import pickle
pickle.dump( {'words':words, 'classes':classes, 'train_x':train_x, 'train_y':train_y}, open( "training_data", "wb" ) )
