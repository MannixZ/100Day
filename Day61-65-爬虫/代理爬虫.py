import re
import requests

APP_KEY = "Wnp******************************XFx"
PROXY_HOST = "secondtransfer.moguproxy.com:9001"


for page in range(1, 11):
    resp = requests.get(
        url=f"https://movie.douban.com/top250?start={(page - 1) * 25}",
        # 需要在HTTP请求头设置代理的身份认证方式
        headers={
            "Proxy-Authorization": f"Basic {APP_KEY}",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
        },
        # 设置代理服务器
        proxies={"http": f"http://{PROXY_HOST}", "https": f"https://{PROXY_HOST}"},
        verify=False,
    )
    pattern1 = re.compile(r'<span class="title">([^&]*?)</span>')
    pattern2 = re.compile(r'<span class="rating_num".*?>(.*?)</span>')
    titles = pattern1.findall(resp.text)
    ranks = pattern2.findall(resp.text)
    for title, rank in zip(titles, ranks):
        print(title, rank)
