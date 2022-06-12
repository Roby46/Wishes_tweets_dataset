# Whishes_tweets_dataset

## Data Organization

## Notes about the data

[Twitter's Terms of Service](https://twitter.com/en/tos).

|               | Before hydration | After hydration |
| ------------- | ------------- | ------------- |
| Number of tweets  | Content Cell  | Content Cell  |
| Number of accounts  | Content Cell  | Content Cell  |
| Number of verified accounts  | Content Cell  | Content Cell  |
| Average tweets per account  | Content Cell  | Content Cell  |
| Account with location  | Content Cell  | Content Cell  |
| Oldest tweet  | Content Cell  | Content Cell  |
| Most recent tweet  | Content Cell  | Content Cell  |
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

## Data Usage Agreement/ How to cite

By using this dataset, you agree to comply with [Twitter's Terms of Service](https://twitter.com/en/tos) and to cite the following article: 

```
@article
```
