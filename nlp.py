
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, MaxPooling1D, Conv1D, GlobalMaxPooling1D, Dropout, LSTM, GRU
from tensorflow.keras import utils
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras import utils
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_group = pd.read_csv(r'C:\Users\000\Desktop\питон\vk_analyieser\file3.csv')
print(df_group['activity'])
activity_dict = df_group.set_index('activity').to_list()
print(len(activity_dict))
df['type'] = 0
