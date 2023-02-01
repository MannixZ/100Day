from lxml import etree
import requests

for page in range(1, 11):
    resp = requests.get(
        url=f"https://movie.douban.com/top250?start={(page - 1) * 25}",
        headers={"User-Agent": "BaiduSpider"},
    )
    tree = etree.HTML(resp.text)

    # 通过XPath语法从页面中提取电影标题
    title_spans = tree.xpath(
        '//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]'
    )
    # 通过XPath语法从页面中提取电影评分
    rank_spans = tree.xpath(
        '//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[2]'
    )
    for title_span, rank_span in zip(title_spans, rank_spans):
        print(title_span, rank_span)
