from lazysdk import lazyrequests


def top_channels():
    api_url = 'https://everest.castbox.fm/data/top_channels/v2'
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Host": "everest.castbox.fm",
        "Origin": "https://castbox.fm",
        "Referer": "https://castbox.fm/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/110.0",
        "X-Web": "true"
    }
    params = {
        'category_id': 
    }
    response = lazyrequests.lazy_requests(
        method='GET',
        url=api_url,

    )

