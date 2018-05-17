import requests
import feedparser
from models.feed import *
from datetime import datetime
from mongoengine import errors

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'cookie': 'aliyungf_tc=AQAAAAPPPSSFqQAAja7seAwB4gaCixDc; _xsrf=5c7e18c6-199a-4e9c-a6c9-66ba7fccdfea; d_c0="ACAtjyhePQ2PTh8A4G08-bVpx9-ZiR6_ESM=|1520236623"; _zap=3cb87be9-369a-4059-bbec-38fd681ad327; __DAYU_PP=6EbiUfUJiNQAZVYZmuJ7ffffffff822d0e2691dd; l_n_c=1; n_c=1; q_c1=4d0fa5bbfd0e4bcfa0860d30f1b7f66a|1525850878000|1520236623000; r_cap_id="NmZiZmI4OTg4MzA1NGNiYzkwNDE0YmVjMjY5ZjNlZTk=|1525850878|60f1954b325b0e61c80aa2d7dc8d96111e9d18e5"; cap_id="MTdjMWMxNTg4YTlmNGMxYjgwYjJjNzNlMTdmMjFkZmI=|1525850878|97b9ed91f4b0636c456db27ac682e202a7df415a"; l_cap_id="NzM1MTgxMDgxOGU4NDlmMjk5YTA2YmQyODRjOWRiMTc=|1525850878|89e8712d43fd96e38cf0bb57f0a2d191933752b9"; tgw_l7_route=bc9380c810e0cf40598c1a7b1459f027; capsion_ticket="2|1:0|10:1526432076|14:capsion_ticket|44:MDUxZDgzY2Q1NjYwNDc4ODllOWVmNjZmMzdjMzg2MGU=|6923f3c4679f23d181a87d85acdb7f48d33b11634fd61785b31da1f8cf82d6c0"; z_c0="2|1:0|10:1526432084|4:z_c0|92:Mi4xS3owY0FRQUFBQUFBSUMyUEtGNDlEU1lBQUFCZ0FsVk5WTV9vV3dCUjFYWmpLVWxMWW1TU1YydHl2bTQzeUVpcUtn|fee3111c3e84e4272146c5f02c2d9978c1053596b4f18ac6fe73a0a1ede01b48"; __utma=155987696.393967868.1526432141.1526432141.1526432141.1; __utmc=155987696; __utmz=155987696.1526432141.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=155987696.6.9.1526432209562',
    # 'cache-control': 'max-age=0',
    # 'if-none-match': '9317fdc738fb23f56b1b9f87bc95e20c839afa99',
    # 'upgrade-insecure-requests':'1',
}
r = requests.get('https://www.zhihu.com/rss', headers=headers)
r.encoding = 'utf-8'


def run():
    f = feedparser.parse(r.text)
    for i in f.entries:
        try:
            Feed(title=i.title, detail=i.description, date=str(
                datetime.now()), source='https://www.zhihu.com/rss').save()
        except(KeyError, AttributeError):
            print(i)
            continue
        except errors.NotUniqueError:
            continue
