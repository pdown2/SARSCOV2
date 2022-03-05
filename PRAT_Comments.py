import datetime as dt
import pandas as pd
import pmaw
import praw
import sys
from pmaw import PushshiftAPI

import datetime as dt
import pandas as pd
from pmaw import PushshiftAPI

api = PushshiftAPI()

# import datetime as dt
# before = int(dt.datetime(2021,2,1,0,0).timestamp())
# after = int(dt.datetime(2020,12,1,0,0).timestamp())

###Subreddit groups being used.
# IsItBecauseOfCovid   -- https://www.reddit.com/r/IsItBecauseOfCovid.json
# CoronaPositive       -- https://www.reddit.com/r/CoronaPositive.json
# COVIDSupportGroup    -- https://www.reddit.com/r/COVIDSupportGroup.json --LIMITED
# Covidhealthcare      -- https://www.reddit.com/r/Covidhealthcare.json
# COVID19_support      -- https://www.reddit.com/r/COVID19_support.json
# COVID19positive      -- https://www.reddit.com/r/COVID19positive.json

subreddit = "COVID19positive"
# subreddit = ['IsItBecauseOfCovid', 'CoronaPositive', 'COVIDSupportGroup', 'Covidhealthcare',\
#             'COVID19_support', 'COVID19positive']
limit = 1
##start and finish date, to limit collection. I wanted everything.
# before = xxxxxxx
# after = xxxxxxx

##uncomment to collect submissions, I was running these individually, you could just create comments2 and append to comments
# search_submissions
# comments = api.search_submissions(subreddit=subreddit, limit=limit)#, before=before, after=after)
# print(f'Retrieved {len(comments)} comments from Pushshift')
# search_comments
comments = api.search_comments(subreddit=subreddit, limit=limit)  # , before=before, after=after)
print(f'Retrieved {len(comments)} comments from Pushshift')

commentsOG1 = pd.DataFrame(comments)
commentsOG1 = commentsOG1[0:0]
commentsOG2 = commentsOG1
commentsOG3 = commentsOG1

# -----------------------------------------------------------------------------------------------------------------------

# SubReddit groups to participate, scope my grow TBD
subreddit_list = ['IsItBecauseOfCovid', 'CoronaPositive', 'COVIDSupportGroup', 'Covidhealthcare']

# comment scrape loop
for group_name in subreddit_list:
    subreddit = group_name
    limit = 500
    # search_submissions
    # search_comments
    comments = api.search_comments(subreddit=subreddit, limit=limit)  # , before=before, after=after) #date limiting TBD
    print(f'Retrieved {len(comments)} comments from {(subreddit)}')

    commentsOG1 = commentsOG1.reset_index(drop=True)

    # append commentsOG from the loop
    commentsOG1 = commentsOG1.append(pd.DataFrame(comments), ignore_index=True)

# grab what we need and make a new df
dfA1 = commentsOG1[['subreddit', 'subreddit_id', 'author', 'body']]

# -----------------------------------------------------------------------------------------------------------------------

# SubReddit groups to participate, scope my grow TBD
subreddit_list = ['COVID19_support']
# Retrieved 176895 comments from COVID19_support

# comment scrape loop
for group_name in subreddit_list:
    subreddit = group_name
    limit = 200000
    # search_submissions
    # search_comments
    comments = api.search_comments(subreddit=subreddit, limit=limit)  # , before=before, after=after) #date limiting TBD
    print(f'Retrieved {len(comments)} comments from {(subreddit)}')

    commentsOG2 = commentsOG2.reset_index(drop=True)

    # append commentsOG from the loop
    commentsOG2 = commentsOG2.append(pd.DataFrame(comments), ignore_index=True)

# grab what we need and make a new df
dfA2 = commentsOG2[['subreddit', 'subreddit_id', 'author', 'body', 'created_utc']]

# -----------------------------------------------------------------------------------------------------------------------

# SubReddit groups to participate, scope my grow TBD
subreddit_list = ['COVID19positive']
# Retrieved 653369 comments from COVID19positive

# comment scrape loop
for group_name in subreddit_list:
    subreddit = group_name
    limit = 1000000
    # search_submissions
    # search_comments
    comments = api.search_comments(subreddit=subreddit, limit=limit)  # , before=before, after=after) #date limiting TBD
    print(f'Retrieved {len(comments)} comments from {(subreddit)}')

    # append commentsOG from the loop
    commentsOG3 = commentsOG3.append(pd.DataFrame(comments), ignore_index=True)

# grab what we need and make a new df
dfA3 = commentsOG3[['subreddit', 'subreddit_id', 'author', 'body', 'created_utc']]

# -----------------------------------------------------------------------------------------------------------------------

# dfA1.head()
len(dfA1.index)
# dfA2.head()
len(dfA2.index)
# dfA2.head()
len(dfA3.index)

df = dfA1.copy()
df = df.append(dfA2)
df = df.append(dfA3)
dfA = df.copy()

len(dfA.index)

# created_utc
# created_utc_str

dfA['datetime'] = pd.to_datetime(dfA['created_utc'], unit='s')  # still want to parse it into a timestamp object
dfA['date'] = dfA['datetime'].dt.strftime('%Y-%m-%d')  # and now we have created a formatted string.

print(dfA.groupby(['subreddit']).count())

dfA.to_csv('./wsb_comments.csv', header=True, index=False, columns=list(dfA.axes[1]))


