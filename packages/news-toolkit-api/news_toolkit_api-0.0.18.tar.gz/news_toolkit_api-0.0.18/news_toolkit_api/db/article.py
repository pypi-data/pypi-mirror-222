from google.cloud import ndb


class RelatedArticle(ndb.Model):
    article_id = ndb.StringProperty(required=True)
    title = ndb.StringProperty(required=True)
    category = ndb.StringProperty(required=True)
    image_url = ndb.StringProperty(required=True)
    auther = ndb.StringProperty()
    published_at = ndb.DateTimeProperty()


class Article(ndb.Model):
    article_id = ndb.StringProperty(required=True)
    title = ndb.StringProperty(required=True)
    content = ndb.TextProperty(repeated=True)
    url = ndb.StringProperty(required=True)
    category = ndb.StringProperty(required=True)
    image_url = ndb.StringProperty()
    auther = ndb.StringProperty()
    published_at = ndb.DateTimeProperty()
    is_premium = ndb.BooleanProperty(default=False)
    is_preview = ndb.BooleanProperty(default=False)
    related_articles = ndb.StructuredProperty(RelatedArticle, repeated=True)
    created_at = ndb.DateTimeProperty(required=True)
