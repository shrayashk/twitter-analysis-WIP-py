import tweepy
from textblob import TextBlob
import csv

consumer_key='UHd1yDX5v9yq1bTWz65o3d4gX'
consumer_secret='NFyyKnVhDd0AOJMaeyg04GNIQD4MV4RMzC3iRNX6e8hY5QQeQs'

access_token='2849029128-1oKmDSoVqKa5IPNP8gAgM0rwgjKGryoUrBsFPee'
access_token_secret='3jnsC0F4JBXsmSwPVV9hooeZZvQHGd0S3LmB0H4h7gkdl'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_sentiment=api.search('Artificial Intelligence',count=1000)

with open('tweets.csv', 'a',encoding="utf-8") as csvFile:
		fields = ['tweets', 'polarity', 'subjectivity']
		writer = csv.writer(csvFile)
		writer.writerow(fields)
		csvFile.close()

for i in public_sentiment:
	list1=[]
	list1.append(i.text)
	analysis=TextBlob(i.text)
	if analysis.sentiment.polarity > 0:
		list1.append('positive')
	elif analysis.sentiment.polarity < 0:
		list1.append('negative')
	else :
		list1.append('absolutely neutral')
	if analysis.sentiment.subjectivity > 0.5:
		list1.append('opinion')
	elif analysis.sentiment.subjectivity < 0.5:
		list1.append('fact')
	else :
		list1.append('statement')
	with open('tweets.csv', 'a',encoding="utf-8") as csvFile:
		writer = csv.writer(csvFile)
		writer.writerow(list1)
		csvFile.close()