from mongoengine import *
from django.conf import settings
connect(settings.DBNAME)

class Post(Document):
    title = StringField(max_length=120, required=True)
    content = StringField(max_length=500, required=True)
    last_update = DateTimeField(required=True)
    tags = ListField(StringField(max_length=30))

