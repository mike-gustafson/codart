from django.core.management.base import BaseCommand
from codart.models import NewsStory
import requests

class Command(BaseCommand):
    help = 'Fetches news stories and saves them to the database'

    def handle(self, *args, **options):
        url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
        response = requests.get(url)
        news_data = response.json()
        print('test')
        for story in news_data['stories']:  # Adjust based on actual response structure
            # Create and save news story to database
            NewsStory.objects.create(
                title=story['title'],
                link=story['url'],
                # add other fields as necessary
            )

        self.stdout.write(self.style.SUCCESS('Successfully saved news stories'))
