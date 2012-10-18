"""This module exposes the XKCD API to Python."""
import urllib2
import json
import datetime

class ComicFetchError(Exception):
    """Raised when something fails to download."""
    pass

XKCD_API = 'https://xkcd.com/%s/info.0.json'
XKCD_URL = 'https://xkcd.com/%s'
class Comic():
    """Get information about comic #num. num=0 refers to the latest comic.

    To use:
    >> comic = Comic(3)
    >> comic.title
    u'Island (sketch)'
    >> latest = Comic(0)

    """
    def __init__(self, num):
        """Grab the data about the comic and save it."""
        if not isinstance(num, int) or num < 0:
            raise ValueError(num)

        # hack to get the latest comic.
        if not num:
            num = '/' 

        try:
            self.data = json.loads(urllib2.urlopen(XKCD_API % num).read())
        except:
            raise ComicFetchError

    @property
    def num(self):
        """Return the comic's number."""
        return self.data['num']

    @property
    def url(self):
        """Return the comic's url."""
        return XKCD_URL % self.num

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
