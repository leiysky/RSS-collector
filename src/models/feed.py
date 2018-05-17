from mongoengine import *
from datetime import datetime as time
connect('feed')


class Feed(Document):
    title = StringField(required=True)
    description = StringField()
    detail = StringField( required=True)
    date = DateTimeField(default=str(time.now()))
    tag = StringField(default='无')
    source = StringField()