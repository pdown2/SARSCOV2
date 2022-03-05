import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

#Import dependencies
import pandas as pd

path = 'subset_100.csv'#'subset_1.csv'#'wsb_comments.csv'#
dfOG = pd.read_csv(path)

dfOG['Address'] = 'NaN'
#to dtype string
dfOG['body'] = dfOG['body'].astype(str)
#all lower cases
dfOG['body'] = dfOG.body.str.replace("[^\w\s]", "").str.lower()
dfOG = dfOG[dfOG['subreddit'].notna()]

## Before removal
#index = dfOG.index
#number_of_rows = len(index)
#print(number_of_rows)

#name = ['covid','covid19','corona','covsar2']
#drop any row on the condition of not having a word present, then merge all 3
df1 = dfOG[dfOG['body'].str.contains(' covid ')]
df2 = dfOG[dfOG['body'].str.contains(' corona ')]
df3 = dfOG[dfOG['body'].str.contains(' covsar2 ')]

df4 = df1.append(df2)
df5 = df4.append(df3)
df5 = df5.drop_duplicates()

## After removal
index = df5.index
number_of_rows = len(index)
print(number_of_rows)

dfC = df5
#dfC


path = 'Vector_sentences.csv'#'subset_1.csv'#'wsb_comments.csv'#
dfS = pd.read_csv(path)
dfS = (dfS[dfS['sentence'].str.contains('covsar2') == False])
dfS = (dfS[dfS['sentence'].str.contains('ive') == False])
dfS = (dfS[dfS['sentence'].str.contains('false positive') == False])

dfC = dfC.reset_index(drop=True)
dfS = dfS.reset_index(drop=True)

dfC["sim"] = np.nan
dfC['body'] = dfC['body'].str.replace('rcovid19_support','')

for t in dfS.index:
    sent = dfS.iloc[t, 0]
    dfC["sim" + str(t)] = np.nan

    for i in dfC.index:
        comment = dfC.iloc[i, 3]
        txts = [sent, comment]  # , txt_control]

        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.feature_extraction.text import TfidfVectorizer

        unigram_count = CountVectorizer(encoding='latin-1', binary=False)
        unigram_count_stop_remove = CountVectorizer(encoding='latin-1', binary=False, stop_words='english')

        vecs = unigram_count.fit_transform(txts)

        from sklearn.metrics.pairwise import linear_kernel

        cos_sim = cosine_similarity(vecs[0], vecs)

        dfC.loc[dfC['body'] == comment, "sim" + str(t)] = str(cos_sim)

df_author = dfC[["author", "body", "sim"]].iloc[:0,:].copy()
print(df_author)
df_author = df_author[["author", "body", "sim"]].append(dfC[["author", "body", "sim0"]], ignore_index = True)
df_author = df_author[["author", "body", "sim"]].append(dfC[["author", "body", "sim1"]], ignore_index = True)
df_author = df_author[["author", "body", "sim"]].append(dfC[["author", "body", "sim2"]], ignore_index = True)
df_author = df_author[["author", "body", "sim"]].append(dfC[["author", "body", "sim3"]], ignore_index = True)
df_author = df_author[["author", "body", "sim"]].append(dfC[["author", "body", "sim4"]], ignore_index = True)
df_author = df_author[["author", "body", "sim"]].append(dfC[["author", "body", "sim5"]], ignore_index = True)

df_mask=df_author['sim5']>=0.08
filtered_df = df_author[df_mask]
#print(filtered_df)

filtered_df.to_csv(r'author_valid.csv', index = False, header = True)


