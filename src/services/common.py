import feedparser as parser
from models.feed import *
from mongoengine import errors as errors

url_list = []


def init(_url):
    global url_list
    url_list = list(_url)


def run():
    for url in url_list:
        print('url: ', url)
        feed = parser.parse(url)
        for i in feed.entries:
            print(i.title)
            try:
                Feed(title=i.title, detail=str(i.content),
                     description=i.description, source=url).save()
            except AttributeError as e:
                if(str(e) == 'object has no attribute \'content\''):
                    # print('谁把文章内容写在description谁是!@#$')
                    try:
                        Feed(title=i.title, detail=str(
                            i.description), source=url).save()
                    except errors.NotUniqueError:
                        continue
            except errors.NotUniqueError:
                continue