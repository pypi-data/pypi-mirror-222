from google.cloud import ndb


class Feed(ndb.Model):
    article_id = ndb.IntegerProperty(required=True)
    title = ndb.StringProperty(required=True)
    category = ndb.StringProperty(required=True)
    image_url = ndb.StringProperty(required=True)
    subtitle = ndb.StringProperty()
    auther = ndb.StringProperty()
    published_at = ndb.DateTimeProperty(required=True)
    created_at = ndb.DateTimeProperty(required=True)
