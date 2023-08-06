import requests

def get_cat_image_url(status_code):
    """
    根据给定的HTTP响应状态代码，返回对应的图片URL。

    参数:
    status_code (str): HTTP响应状态代码，如 "200"。

    返回:
    str: 对应状态代码的图片URL。
    """
    # 判断输入的状态代码是否为三位数字
    if not status_code.isdigit() or len(status_code) != 3:
        raise ValueError("HTTP响应状态代码必须是一个三位数字字符串。")

    # 构建图片URL
    image_url = f"https://httpcats.com/{status_code}.jpg"

    return image_url

def download_cat_image(url):
    """
    根据给定的URL下载图片并保存在变量中。

    参数:
    url (str): 图片的URL。

    返回:
    bytes: 图片内容的字节数据。
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        raise ValueError("无法下载图片。")

def get_cat_image(status_code, image_format=".jpg"):
    """
    根据输入的状态代码和图片格式返回对应的图片。

    参数:
    status_code (str): HTTP响应状态代码，如 "200"。
    image_format (str): 图片格式，可以是 ".jpg", ".webp", ".jxl", ".avif" 或 ".json"。

    返回:
    bytes: 图片内容的字节数据。
    """
    # 获取对应状态代码的图片URL
    image_url = get_cat_image_url(status_code)

    # 下载图片并保存在变量中
    image_bytes = download_cat_image(image_url)

    return image_bytes
