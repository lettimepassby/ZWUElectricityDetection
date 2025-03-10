# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import datetime

PUSHPLUS_TOKEN = ""  # 请替换成你自己的 token
PUSHPLUS_API = "http://www.pushplus.plus/send"

def push_to_pushplus(title, content):
    """
    调用 pushplus 接口，向个人微信发送消息
    """
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "token": PUSHPLUS_TOKEN,
        "title": title,
        "content": content,
        "template": "html"  # 可选：html、txt、json 等，看个人需要
    }
    try:
        resp = requests.post(PUSHPLUS_API, json=data, headers=headers, timeout=10)
        resp.raise_for_status()
        print("pushplus 消息推送成功！")
    except Exception as e:
        print("pushplus 消息推送失败：", e)


def get_electricity_balance():
    """
    从 jkschool.lsmart.cn/electric/electric_goAmount.shtml 查询指定房间的电量信息
    返回值: 返回剩余电量数字(例如 36.0)，出错或未获取到返回 None
    """
    url = "https://jkschool.lsmart.cn/electric/electric_goAmount.shtml"
    # POST 表单数据
    payload = {
        "openId": "替换成你的",
        "wxArea": "替换成你的",
        "areaNo": "替换成你的",
        "buildNo": "替换成你的",
        "roomNo": "替换成你的"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.post(url, data=payload, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"请求失败：{e}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    balance_tag = soup.find("span", class_="font-16 elet-num")
    if not balance_tag:
        print("未能在返回的页面中找到剩余电量信息。")
        return None

    # balance_tag 形如 "36.0 度"
    balance_text = balance_tag.get_text(strip=True)  # "36.0 度"
    # 去掉“度”等字符，只保留数字部分，做 float 转换
    # 常见格式可能是 "36.0 度", "5 度", "8.5 度"...
    try:
        balance_value = float(balance_text.replace("度", "").strip())
    except ValueError:
        print("无法将电量信息转换为数字。原始文本：", balance_text)
        return None

    return balance_value

if __name__ == "__main__":
    electricity_balance = get_electricity_balance()
    now = datetime.datetime.now()

    if electricity_balance is not None:
        print(f"查询到的剩余电量: {electricity_balance} 度")
        # 1. 如果当前电量 < 5，则发推送
        if electricity_balance < 5:
            msg_title = "电量过低提醒"
            msg_content = f"当前剩余电量仅 {electricity_balance} 度，请及时充值。"
            push_to_pushplus(msg_title, msg_content)

        # 2. 如果当前时间是早上 8 点，也发推送（可根据实际需求再细化是否只在 8:00 整推）
        #    这里判断只要是 hour == 8 即推送，你也可以加上: now.minute == 0
        #    这样可以确保只有在 8:00 才推送。
        if now.hour == 8 and now.minute == 0:
            msg_title = "每日例行电量提醒"
            msg_content = f"现在是早上 8 点整，当前电量为 {electricity_balance} 度。"
            push_to_pushplus(msg_title, msg_content)

    else:
        print("查询失败或未获取到电量信息。")
