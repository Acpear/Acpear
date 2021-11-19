import requests
from lxml import etree

if __name__ == '__main__':
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/95.0.4638.69 Safari/537.36',
        'Cookie': 'Your Cookie',
    }
    url = 'https://s.weibo.com/top/summary?cate=realtimehot'
    req = etree.HTML(requests.get(url=url, headers=header).text)
    tbody = req.cssselect('tbody')[0]
    news_rank = []
    news_name = []
    news_view = []
    for item in tbody.cssselect('tr'):
        if item.cssselect('.td-01')[0].text is None:
            news_rank.append('Top')
            news_name.append(item.cssselect('.td-02 a')[0].text)
            news_view.append('')
        elif item.cssselect('.td-01')[0].text != '•':
            news_rank.append(str(item.cssselect('.td-01')[0].text))
            news_name.append(str(item.cssselect('.td-02 a')[0].text))
            news_view.append(str(item.cssselect('.td-02 span')[0].text))
    for i in range(len(news_rank)):
        print(news_rank[i], news_name[i], news_view[i])