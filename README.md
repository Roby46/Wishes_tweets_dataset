# Whishes_tweets_dataset

## Data Organization

## Notes about the data

[Twitter's Terms of Service](https://twitter.com/en/tos).

|               | Before hydration | After hydration |
| ------------- | ------------- | ------------- |
| Number of tweets  | 4.489.070  | 3.760.574  |
| Number of accounts  | -  | 1.170.868  |
| Number of verified accounts  | -  | 17.537  |
| Average tweets per account  | -  | 3,21  |
| Account with location  | -  | 2.468.532  |
| Oldest tweet  | Content Cell  | Content Cell  |
| Most recent tweet  | 2022-02-25  | 2022-02-25  |
## How to Hydrate

### Hydrating using Hydrator (GUI)

### Hydrating using Twarc (CLI)

First install [twarc](https://twarc-project.readthedocs.io/en/latest/) and [tqdm](https://tqdm.github.io/)

```
pip3 install twarc
pip3 install tqdm
```

Configure twarc with your Twitter API tokens (you must apply for a Twitter developer account first in order to generate these tokens). You can also configure the API tokens by running the command:

```
twarc configure
```
Then you can run the script. The hydrated tweets will be stored in the same folder that contains the tweets' IDs as a compressed jsonl file. 

### Hydrating using Tweepy
```
import tweepy
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, retry_count=5, retry_delay=2, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
api.statuses_lookup(list_of_ids) #consider the limitations in tweepy documentation
```
## Data Usage Agreement/ How to cite

By using this dataset, you agree to comply with [Twitter's Terms of Service](https://twitter.com/en/tos) and to cite the following article: 

```
@article
```
