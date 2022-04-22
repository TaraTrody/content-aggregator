from django.core.management.base import BaseCommand

import feedparser
from dateutil import parser

from podcasts.models import Episode
class Command(BaseCommand):
    def handle(self, *args, **options): 
        feed = feedparser.parse("https://realpython.com/podcasts/rpp/feed")
        podcast_title = feed.channel.title  
        podcast_image = feed.channel.image["href"]
        # TODO: iterate over feed entries:
            # if the entry doesn't exists, extract the podcast data
            # save to the database