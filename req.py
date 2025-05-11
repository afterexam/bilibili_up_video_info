import requests

# URL
url = "https://api.bilibili.com/x/space/wbi/arc/search"




# 请求头
headers = {
    "Host": "api.bilibili.com",
    "Connection": "keep-alive",
    "sec-ch-ua-platform": "\"Windows\"",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Microsoft Edge\";v=\"134\"",
    "DNT": "1",
    "sec-ch-ua-mobile": "?0",
    "Accept": "*/*",
    "Origin": "https://space.bilibili.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://space.bilibili.com/254463269/upload/video",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    # "Cookie": "DedeUserID=49812229; DedeUserID__ckMd5=33e8fe17a8a37f44; ...; SESSDATA=..."
}

page = 1
# mid = 686127 # 籽岷的UID

mid =254463269 #毕导
# GET 请求参数

# 发送 GET 请求
from rev import reverse
for i in range(1,1000):
    signed_params = reverse(i,mid )
    response = requests.get(url, params=signed_params, headers=headers)

    # 输出返回结果
    print(response.status_code)
    print(response.text)
