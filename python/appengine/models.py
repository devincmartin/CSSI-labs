from google.appengine.ext import ndb

class MemeInfo(ndb.Model):
    meme_url = ndb.StringProperty(required=True)
    top_line = ndb.StringProperty(required=True)
    bottom_line = ndb.StringProperty(required=True)
