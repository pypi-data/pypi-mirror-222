from lxml import etree
import requests
import json
import re


def get_html_with_proxies(
        url,
        proxies=None,
        cookie=None
):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Host": "www.youtube.com",
        "Cookie": "YSC=G_3GwXy0TzA; GPS=1; VISITOR_INFO1_LIVE=7Q4YGkHmVbw; PREF=f4=4000000&f6=40000000&tz=Asia.Shanghai&f7=100; GOOGLE_ABUSE_EXEMPTION=ID=69d89e7bc441b9f2:TM=1678375694:C=r:IP=2400:8902::f03c:93ff:fe9f:6fd5-:S=-q3H5EY1xm5wr6h54FNbpe8",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/110.0"
    }
    if cookie:
        headers['Cookie'] = cookie
    response = requests.get(
        url=url,
        headers=headers,
        proxies=proxies,
        timeout=10,
        verify=False
    )
    return response.text


def clean_ytInitialPlayerResponse(
        ytInitialPlayerResponse_json: dict
):
    """
    清洗ytInitialPlayerResponse的内容，获取需要的数据
    :param ytInitialPlayerResponse_json:
    :return:
    """
    clean_res = dict()

    # responseContext = ytInitialPlayerResponse_json.get('responseContext')  # 非关键
    # playabilityStatus = ytInitialPlayerResponse_json.get('playabilityStatus')  # 非关键
    streamingData = ytInitialPlayerResponse_json.get('streamingData')  # 视频流信息，可以供下载视频使用
    # playerAds = ytInitialPlayerResponse_json.get('playerAds')  # 非关键
    # playbackTracking = ytInitialPlayerResponse_json.get('playbackTracking')  # 非关键
    captions = ytInitialPlayerResponse_json.get('captions')  # 视频字幕信息，可下载字幕内容
    videoDetails = ytInitialPlayerResponse_json.get('videoDetails')  # 视频基本信息，重要，含有浏览次数
    # playerConfig = ytInitialPlayerResponse_json.get('playerConfig')  # 非关键
    # storyboards = ytInitialPlayerResponse_json.get('storyboards')  # 非关键
    microformat = ytInitialPlayerResponse_json.get('microformat')  # 含有分类信息和视频信息，有用
    # trackingParams = ytInitialPlayerResponse_json.get('trackingParams')  # 非必要
    # attestation = ytInitialPlayerResponse_json.get('attestation')  # 非必要
    # videoQualityPromoSupportedRenderers = ytInitialPlayerResponse_json.get('videoQualityPromoSupportedRenderers')  # 非必要 支持/帮助信息
    # adPlacements = ytInitialPlayerResponse_json.get('adPlacements')  # 非必要，广告内容

    clean_res['author'] = videoDetails.get('author')  # 作者
    clean_res['channelId'] = videoDetails.get('channelId')
    clean_res['lengthSeconds'] = videoDetails.get('lengthSeconds')  # 时常：秒
    clean_res['shortDescription'] = videoDetails.get('shortDescription')  # 简介
    clean_res['title'] = videoDetails.get('title')  # 标题
    clean_res['videoId'] = videoDetails.get('videoId')  # 视频id
    clean_res['viewCount'] = videoDetails.get('viewCount')  # 观看人数

    clean_res['publishDate'] = microformat.get('playerMicroformatRenderer').get('publishDate')  # 发布时间
    clean_res['uploadDate'] = microformat.get('playerMicroformatRenderer').get('uploadDate')  # 上传时间
    clean_res['category'] = microformat.get('playerMicroformatRenderer').get('category')  # 分类
    clean_res['ownerProfileUrl'] = microformat.get('playerMicroformatRenderer').get('ownerProfileUrl')  # 作者主页

    clean_res['streamingData'] = streamingData
    clean_res['thumbnails'] = videoDetails.get('thumbnail').get('thumbnails')  # 封面图，默认下载"height": 188,"width": 336
    clean_res['captions'] = captions  # 字幕信息captionTracks.baseUrl是基础，加上&fmt=json3&xorb=2&xobt=3&xovt=3&tlang=zh-Hans可以翻译为简体中文

    return clean_res


def initial_player_response(
        url: str,
        proxies=None,
        html_text=None
):
    """
    获取播放信息
    :param url:
    :param proxies:
    :param html_text:
    :return:
    """
    if html_text:
        page_source_code = html_text
    else:
        page_source_code = get_html_with_proxies(
            url=url,
            proxies=proxies
        )  # 页面源码
    tree = etree.HTML(page_source_code, etree.HTMLParser())
    scripts = tree.xpath('/html/body/script/text()')
    for script in scripts:
        if 'var ytInitialPlayerResponse = ' in script:
            ytInitialPlayerResponse = re.findall('var ytInitialPlayerResponse = (.*?);var ', script, re.S)[0]
            ytInitialPlayerResponse_json = json.loads(ytInitialPlayerResponse)
            return ytInitialPlayerResponse_json


def initial_data(
        url: str,
        proxies=None,
        html_text=None
):
    if html_text:
        page_source_code = html_text
    else:
        page_source_code = get_html_with_proxies(
            url=url,
            proxies=proxies
        )  # 页面源码
    # print(page_source_code)
    scripts = re.findall('<script(.*?)</script>', page_source_code, re.S)
    for script in scripts:
        # print(script)
        if 'var ytInitialData = ' in script:
            # print(script)
            # ytInitialData = script.replace('var ytInitialData = ', '')
            ytInitialData = re.findall('var ytInitialData = (.*?)$', page_source_code, re.S)[0]
            print(ytInitialData)
            ytInitialData_json = json.loads(ytInitialData[:-1])
            return ytInitialData_json


def main():
    url = ''
    res = initial_data(
        url=url,

    )
    print(res)


if __name__ == '__main__':
    main()