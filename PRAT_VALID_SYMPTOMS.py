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



## After removal
index = dfOG.index
number_of_rows = len(index)
print(number_of_rows)

dfC = dfOG
#dfC

path = 'author_valid.csv'#'subset_1.csv'#'wsb_comments.csv'#
dfA = pd.read_csv(path)

dfAA = dfA[['author']]
dfAA.drop_duplicates(subset ="author",
                     keep = False, inplace = True)
dfAA.head()

path = 'symptoms.csv'#'subset_1.csv'#'wsb_comments.csv'#
dfS = pd.read_csv(path)

dfC = dfC.reset_index(drop=True)
dfS = dfS.reset_index(drop=True)
dfAA = dfAA.reset_index(drop=True)

dfCC = dfC[~dfC['author'].isin(dfAA['author'])]

#dfCC['body'].iloc[0]
dfCC = dfCC.reset_index(drop=True)

for t in dfS.index:
    sent = dfS.iloc[t, 2]
    dfCC["sim" + str(t)] = np.nan
    # print(sent)

    for i in dfCC.index:
        comment = dfCC.iloc[i, 3]
        txts = [sent, comment]  # , txt_control]

        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.feature_extraction.text import TfidfVectorizer

        unigram_count = CountVectorizer(encoding='latin-1', binary=False)
        unigram_count_stop_remove = CountVectorizer(encoding='latin-1', binary=False, stop_words='english')

        vecs = unigram_count.fit_transform(txts)

        from sklearn.metrics.pairwise import linear_kernel

        cos_sim = cosine_similarity(vecs[0], vecs)

        dfCC.loc[dfC['body'] == comment, "sim" + str(t)] = str(cos_sim)



for t in dfS.index:
    dfCC["sim"+str(t)] = dfCC["sim"+str(t)].astype(str)
    dfCC["sim"+str(t)] = dfCC["sim"+str(t)].str.replace('[#,@,&]','')
    dfCC["sim"+str(t)] = dfCC["sim"+str(t)].str.replace("]]",'')
    dfCC["sim"+str(t)] = dfCC["sim"+str(t)].str[4:]
    dfCC["sim"+str(t)] = dfCC["sim"+str(t)].astype(object)
    dfCC["sim"+str(t)] = pd.to_numeric(dfCC["sim"+str(t)],errors='coerce')

dfCC.to_csv(r'symptoms_all_returns.csv', index = False, header = True)

df_symptoms = dfCC[["author", "body", "sim0"]].iloc[:0,:].copy()
df_symptoms = df_symptoms.reset_index(drop=True)
#df_symptoms = dfCC[["author", "body", "sim"]].iloc[:0].copy()

df_symptoms = df_symptoms.reset_index(drop=True)
print(df_symptoms)

df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim0"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim1"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim2"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim3"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim4"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim5"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim6"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim7"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim8"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim9"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim10"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim11"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim12"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim13"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim14"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim15"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim16"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim17"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim18"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim19"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim20"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim21"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim22"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim23"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim24"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim25"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim26"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim27"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim28"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim29"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim30"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim31"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim32"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim33"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim34"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim35"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim36"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim37"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim38"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim39"]], ignore_index = True)
df_symptoms = df_symptoms[["author", "body", "sim0"]].append(dfCC[["author", "body", "sim40"]], ignore_index = True)

df_mask=df_symptoms['sim0']>=0.08
filtered_df = df_symptoms[df_mask]
print(filtered_df)

filtered_df.to_csv(r'symptoms_valid.csv', index = False, header = True)