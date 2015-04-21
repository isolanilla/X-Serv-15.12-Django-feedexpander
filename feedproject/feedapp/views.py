from django.shortcuts import render
from django.http import HttpResponse
import feedparser
# Create your views here.
def mifeed(request,username):
	url =  "https://twitrss.me/twitter_user_to_rss/?user=" + username
	dicc = feedparser.parse(url)
	salida = ""
	for number in range(5):
		salida += dicc.entries[number].title + "<br>"

	return HttpResponse()