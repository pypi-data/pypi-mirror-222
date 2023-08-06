from google.cloud import ndb


class Category(ndb.Model):
    name = ndb.StringProperty(required=True)
