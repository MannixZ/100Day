import requests
import re
import time
import random

for page in range(1, 11):
    resp = requests.get(
        url=f"https://movie.douban.com/top250?start={(page - 1) * 25}",
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
        },
    )
    pattern1 = re.compile(r'<span class="title">([^&]*?)</span>')
    pattern2 = re.compile(r'<span class="rating_num".*?>(.*?)</span>')
    titles = pattern1.findall(resp.text)
    ranks = pattern2.findall(resp.text)
    for title, rank in zip(titles, ranks):
        print(title, rank)
    time.sleep(random.random() * 4 + 1)
