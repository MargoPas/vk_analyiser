
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, MaxPooling1D, Conv1D, GlobalMaxPooling1D, Dropout, LSTM, GRU
from tensorflow.keras import utils
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras import utils
from sklearn import preprocessing
le = preprocessing.LabelEncoder()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
nltk.download('punkt')
nltk.download('popular')
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()
nltk.download("stopwords")
from nltk.corpus import stopwords
from string import punctuation
russian_stopwords = stopwords.words("russian")

# Удаление знаков пунктуации из текста
def remove_punct(text):
    table = {33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ', 45: ' ', 46: ' ', 47: ' ', 58: ' ', 59: ' ', 60: ' ', 61: ' ', 62: ' ', 63: ' ', 64: ' ', 91: ' ', 92: ' ', 93: ' ', 94: ' ', 95: ' ', 96: ' ', 123: ' ', 124: ' ', 125: ' ', 126: ' '}
    return text.translate(table)




df_group = pd.read_csv(r'./file3.csv')
print(df_group)
df = df_group[df_group['activity'].map(df_group['activity'].value_counts()) > 60]

le.fit(df['activity'])
number_activity = le.transform(df['activity'])
df.insert(loc=0, column='number_activity', value=number_activity)

# Максимальное количество слов
num_words = 10000
# Максимальная длина новости
max_news_len = 100
# Количество классов новостей
nb_classes = max(number_activity)
df['helper'] = ' '
text = df['name'] + df['helper'] + df['description'] + df['helper'] + df['status']
print(text)
text = text.astype('str')

df['text_clean'] = text.map(lambda x: x.lower())
df['text_clean'] = df['text_clean'].map(lambda x: remove_punct(x))
df['text_clean'] = df['text_clean'].map(lambda x: x.split(' '))
df['text_clean'] = df['text_clean'].map(lambda x: [token for token in x if token not in russian_stopwords\
                                                                  and token != " " \
                                                                  and token.strip() not in punctuation])
df['text_clean'] = df['text_clean'].map(lambda x: ' '.join(x))
text = pd.DataFrame(df['text_clean'].apply(nltk.word_tokenize))
print(text)
for index, row in text.iterrows():
    for w in text['text_clean'][index]:
        wordnet_lemmatizer.lemmatize(w)
'''
y_train = utils.to_categorical(df['number_activity'] - 1, nb_classes)
print(y_train)
tokenizer = Tokenizer(num_words = num_words)
tokenizer.fit_on_texts(text)
tokenizer.word_index
sequences = tokenizer.texts_to_sequences(text)
x_train = pad_sequences(sequences, maxlen=max_news_len)
print(x_train)

model_gru = Sequential()
model_gru.add(Embedding(num_words, 32, input_length=max_news_len))
model_gru.add(GRU(16))
model_gru.add(Dense(nb_classes, activation='softmax'))
model_gru.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model_gru.summary()
model_gru_save_path = 'best_model_gru.h5'
checkpoint_callback_gru = ModelCheckpoint(model_gru_save_path,
                                      monitor='val_accuracy',
                                      save_best_only=True,
                                      verbose=1)
history_gru = model_gru.fit(x_train,
                              y_train,
                              epochs=100,
                              batch_size=128,
                              validation_split=0.1,
                              callbacks=[checkpoint_callback_gru])
print(history_gru)

plt.plot(history_gru.history['accuracy'],
         label='Доля верных ответов на обучающем наборе')
plt.plot(history_gru.history['val_accuracy'],
         label='Доля верных ответов на проверочном наборе')
plt.xlabel('Эпоха обучения')
plt.ylabel('Доля верных ответов')
plt.legend()
plt.show()
'''