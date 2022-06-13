import tweepy
import time

api_key =  ''
api_secret_key = ''
access_token =  ''
access_token_secret =  ''

keywords = ['#abolish522', '#abuseisnotlove', '#abuseisnotloveandloveisnotabuse', '#abuserecovery', '#abusesurvivor', '#breakup', '#bringbackourgirls',
'#changethestigma', '#childcustody', '#children', '#codependent', '#coparenting', '#divorce', '#divorceadvice', '#divorcecommunity',
'#divorced', '#divorcedmom', '#divorcehelp', '#divorcequotes', '#divorcerecovery', '#divorcesupport', '#domesticabuse',
'#domesticabusesurvivor', '#domesticviolence', '#emotionalabuse', '#emotionalabusesurvivor', '#emotionalhealing', '#emotionallyhealthy',
'#empath', '#empower', '#empoweredwomen', '#endsars', '#everydaysexism', '#generationequality', '#girlbossquotes', '#heal', '#healer',
'#healing', '#healingyourself', '#healthyrelationships', '#heartbroken', '#heforshe', '#huiselijkgeweld', '#ifmywoundswerevisible',
'#innerwork', '#intuitivehealer', '#istanbulconventionsaveslives', '#iwillgoout', '#knowyourworth', '#lawofattraction', '#lettinggo',
'#lightworker', '#linda', '#loveyourselfik', '#loveyourselfquotes', '#loveyourselfyep', '#manifesting', '#metoo', '#movingon',
'#narcissisticabuse', '#narcissisticabuserecovery', '#narcissisticabusesurvivor', '#narcissisticbehaviour', '#narcproofandthrivingthe',
'#neverforget', '#niunamenos', '#olcayonderzoekt', '#orangetheworld', '#positivevibes', '#quoteoftheday', '#raiseawareness',
'#relationshipadvice', '#relationships', '#ripamina', '#selflove', '#separation', '#singlemom', '#singlemum', '#singleparent',
'#singleparenting', '#soulhealing', '#stopfeminicides', '#strongereveryday', '#strongwomen', '#superwoman', '#survivor', '#survivorprivilege',
'#tequilanotthelime', '#theemptychair', '#therapy', '#timesup', '#toxicpeople', '#toxicrelationships', '#traumabonding', '#trustinyourself',
'#undress522', '#unmaskingmovement', '#walkaway', '#warrior', '#whitewednesdays', '#whyistayed', '#women4women',
'#womensempowerment', '#womenshould', '#womensupportingwomen', '#wordporn', '#wordsofwisdom', '#workingwomen', '#yesallwomen', '#youareenough',
'#youarenotalone', '#youdeservemore', '#yougotthis']

class IDPrinter(tweepy.Stream):
    ids = []
    def on_status(self, status):
        self.ids.append(str(status.id))
        if len(self.ids) % 10 == 0:
            datetime = time.strftime("%d-%m-%y")
            with open("./"+str(datetime)+".txt", "a") as f:
                print(self.ids)
                for id in self.ids:
                    f.write(id+"\n")
                self.ids = []
        #print(status.id)

printer = IDPrinter(
  api_key, api_secret_key,
  access_token, access_token_secret
)
printer.filter(track=keywords)



