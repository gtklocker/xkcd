"""Tiny library to grab XKCD comic information."""
import urllib2
import json
import datetime

class xkcdComic:
    def __init__( self, num ):
        self.num = num
        self.api = 'https://xkcd.com/%s/info.0.json' % self.num
        self.url = 'https://xkcd.com/%s' % self.num

        try:
            self.data = json.loads( urllib2.urlopen( self.api ).read() )
        except:
            print( 'Something\'s wrong with the internet.' )

    @property
    def num( self ):
        return self.num
    def url( self ):
        return self.url
    def img( self ):
        return self.data[ 'img' ]
    def title( self ):
        return self.data[ 'title' ]
    def alt( self ):
        return self.data[ 'alt' ]
    def transcript( self ):
        return self.data[ 'transcript' ]
    def when( self ):
        return datetime.date( int( self.data[ 'year' ] ), \
                              int( self.data[ 'month' ] ), \
                              int( self.data[ 'day' ] ) )
