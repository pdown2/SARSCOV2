
import pandas as pd
import tensorflow_hub as hub
import numpy as np

import texthero as hero
from texthero import preprocessing


df = pd.DataFrame(columns = ['sentence'])
list = []

# different names for COVID
name = ['covid', 'corona', 'covsar2']

# search sentences
sent = ['positive for name', 'i had name', 'i have name', 'ive got name', 'ive had name', 'i got name', \
        'tested positive for name', 'i am name positive', 'im positive for name', 'i have a false positive for name']

for t in name:
    nameT = (t)

    for i in sent:
        sentT = (i)
        sentence1 = (sentT.replace("name", nameT))
        df.loc[len(df.index)] = sentence1

df.head()

#download the model
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5")

df['tsneuse'] = hero.tsne(df['use'])

df.to_csv (r'Vector_sentences.csv', index = False, header=True)