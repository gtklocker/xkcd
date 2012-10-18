"""This module exposes the XKCD API to Python."""
import urllib2
import json
import datetime

class Comic():
    """Get information about comic #num."""
    def __init__(self, num):
        """Grab the data about the comic and save it."""
        self.num = num
        self.api = 'https://xkcd.com/%s/info.0.json' % self.num
        self.url = 'https://xkcd.com/%s' % self.num

        try:
            self.data = json.loads(urllib2.urlopen(self.api).read())
        except:
            print('Something\'s wrong with the internet.')

    @property
    def num(self):
        """Return the comic's number."""
        return self.num

    @property
    def url(self):
        """Return the comic's url."""
        return self.url

    @property
    def img(self):
        """Return the comic's image url."""
        return self.data['img']

    @property
    def title(self):
        """Return the comic's title."""
        return self.data['title']

    @property
    def alt(self):
        """Return the comic's alt."""
        return self.data['alt']

    @property
    def transcript(self):
        """Return the comic's transcript."""
        return self.data['transcript']

    @property
    def when(self):
        """Return when the comic was posted."""
        return datetime.date(int(self.data['year']),
                             int(self.data['month']),
                             int(self.data['day']))
