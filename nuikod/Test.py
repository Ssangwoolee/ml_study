import requests
from pandas.io.json import json_normalize

# chrome, 화면, f12 - 개발자 윈도우, xhr
# 화면에서 page를 갱신하면서 어떻게 request를 넣는지 보고 이를 통해서 server로 부터 data를 받아온다.
# crawling test 할 때 mobile version에서 하면 data가 좀 준다.


def make_url(pagesize=10, page=1):
    return "https://m.stock.naver.com/api/json/sise/siseListJson.nhn?menu=market_sum&sosok=0&pageSize=" + str(pagesize) + "20&page=" + str(page)


def get_data(url):
    response = requests.get(url)
    json_info = response.json()
    companies = json_info["result"]["itemList"]
    df = json_normalize(companies)
    return df


result = get_data(make_url())
print(result)
