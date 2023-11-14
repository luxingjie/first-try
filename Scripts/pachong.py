# XingJieXingjie
import requests
from bs4 import BeautifulSoup

# 目标网页的URL
url = 'https://www.youtube.com/watch?v=gPErX8EnIiU'

# 发送HTTP请求
response = requests.get(url)

# 确认请求成功，状态码为200
if response.status_code == 200:
    # 解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 从网页中提取数据
    # 假设我们想提取网页标题
    title = soup.find('title').text

    print('网页标题:', title)
else:
    print('请求失败，状态码:', response.status_code)