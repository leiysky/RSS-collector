from services import zhihu
from services import common

def runner(func_list):
    for i in func_list:
        try:
            i()
        except():
            continue


run_list = (
    zhihu.run,
    common.run,
)

url_list = ['http://songshuhui.net/feed',
            # 'http://www.scipark.net/feed/', # 挂掉了
            'http://pansci.tw/feed',
            'http://www.matrix67.com/blog/feed.asp',
            'http://feed.read.org.cn/',
            # 'http://cnpolitics.org/feed/', # 不符合标准，没有<rss>节点
            'http://www.duxieren.com/duxieren.xml',
            'http://feed.williamlong.info/',
            'https://cn.engadget.com/rss.xml',
            'http://36kr.com/feed',
            'https://sspai.com/feed',
            'http://www.toodaylab.com/feed',
            'http://cinephilia.net/feed',
            'http://www.uisdc.com/feed',
            'http://huo360.com/feed',
            ]

if (__name__ == '__main__'):
    common.init(url_list)
    runner(run_list)
        
