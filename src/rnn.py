# Due to the size of the data, this cell takes about two hours to be run
#%%
import pandas as pd
df=pd.read_csv('../data/cleanedtrain.csv')
#%%
df.drop(['Unnamed: 0','question_title','question_content','best_answer'],axis=1,inplace=True)

#%%
def build_dic(df,cleaned_data, classes):
  dic = {}
  for cls in classes:
    dic[cls] = []
  for i in range(df.shape[0]):
    raw = df.loc[i]
    dic[raw.label].append((cleaned_data[i], raw.best_answer))
  return dic
# %%

# LSTM for sequence classification in the IMDB dataset
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing import sequence
# fix random seed for reproducibility
tf.random.set_seed(7)
# load the dataset but only keep the top n words, zero the rest
top_words = 5000
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=top_words)

#%%
# truncate and pad input sequences
max_review_length = 500
X_train = sequence.pad_sequences(X_train, maxlen=max_review_length)
X_test = sequence.pad_sequences(X_test, maxlen=max_review_length)
#%%
X_train

#%%
# create the model
embedding_vecor_length = 32
model = Sequential()
model.add(Embedding(top_words, embedding_vecor_length, input_length=max_review_length))
model.add(LSTM(100))
model.add(Dense(10, activation='softmax'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())
model.fit(X_train, y_train, epochs=3, batch_size=64)
# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))
# %%
