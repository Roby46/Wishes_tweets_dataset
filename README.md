# Wishes (Women Inclusion and Safety for Holding Equality in Society) Tweets Dataset

This repository contains a collection of tweets on the topic of women inclusion and safety. The tweets were obtained using the Twitter API to capture tweets with hashtags related to the topic in question. The exploited keywords are visible in the script listener streamlistener_domestic_violence.py. In accordance with [Twitter's Terms of Service](https://twitter.com/en/tos), only tweet IDs are present in the repository. The data is for non-commercial research purposes only. 
The paper related to this repository can be found [here]().

## Data Organization

The Tweets_IDs folder includes files containing the tweet IDs. The tweets are organized in files by day so that each file contains only the tweets written on the day indicated in the file name. The files are 82 in all and they are in txt format.

## Notes about the data
This dataset contains tweets written in 64 different languages. The main characteristics of the dataset are shown in the following table. For detailed instructions about how to hydrate these tweets, see the next section.

|               | Before hydration | After hydration |
| ------------- | ------------- | ------------- |
| Number of tweets  | 4.489.070  | 3.760.574  |
| Number of accounts  | -  | 1.170.868  |
| Number of verified accounts  | -  | 17.537  |
| Average tweets per account  | -  | 3,21  |
| Account with location  | -  | 2.507  |
| Oldest tweet  | 2021-11-10  | 2021-11-10  |
| Most recent tweet  | 2022-02-25  | 2022-02-25  |
## How to Hydrate

### Hydrating using Hydrator (GUI)

Navigate to the [Hydrator github repository](https://github.com/DocNow/hydrator) and follow the instructions for installation in their README. As there are a lot of separate Tweet ID files in this repository, it might be advisable to first merge files from timeframes of interest into a larger file before hydrating the Tweets through the GUI.

### Hydrating using Twarc (CLI)

First install [twarc](https://twarc-project.readthedocs.io/en/latest/) and [tqdm](https://tqdm.github.io/)

```
pip3 install twarc
pip3 install tqdm
```

Configure twarc with your Twitter API tokens (you must apply for a Twitter developer account first in order to generate these tokens). You can configure the API tokens by running the command:

```
twarc configure
```
Then you can run the script. The hydrated tweets will be stored in the same folder that contains the tweets' IDs as a compressed jsonl file. 
```
python3 hydrate.py -credentials
```


### Hydrating using Tweepy
```
import tweepy
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, retry_count=5, retry_delay=2, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
api.statuses_lookup(list_of_ids) 
```
## Data Usage Agreement/ How to cite

By using this dataset, you agree to comply with [Twitter's Terms of Service](https://twitter.com/en/tos) and to cite the following article: 

```
@inproceedings{caruccio2022women,
  title={Data Analytics on Twitter for Evaluating Women Inclusion and Safety in Modern Society.},
  author={Caruccio, L., Cirillo, S., Deufemia, V., Polese, G., and Stanzione R.},
  booktitle={TBD},
  year={2022}
}
```
