import requests

def get_image_url(service, status_code, image_format=".jpg"):
    """
    根据给定的服务和HTTP响应状态代码，返回对应的图片URL。

    参数:
    service (str): 图片服务，可以是 "httpcats" 或 "httpdog"。
    status_code (str): HTTP响应状态代码，如 "200"。
    image_format (str): 图片格式，可以是 ".jpg", ".webp", ".jxl", ".avif" 或 ".json"。

    返回:
    str: 对应状态代码的图片URL。
    """
    # 判断输入的状态代码是否为三位数字
    if not status_code.isdigit() or len(status_code) != 3:
        raise ValueError("HTTP响应状态代码必须是一个三位数字字符串。")

    # 构建图片URL
    base_url = "https://httpcats.com" if service == "httpcats" else "https://http.dog"
    image_url = f"{base_url}/{status_code}{image_format}"

    return image_url

def download_image(url):
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

def get_image(service, status_code, image_format=".jpg"):
    """
    根据输入的服务、状态代码和图片格式返回对应的图片。

    参数:
    service (str): 图片服务，可以是 "httpcats" 或 "httpdog"。
    status_code (str): HTTP响应状态代码，如 "200"。
    image_format (str): 图片格式，可以是 ".jpg", ".webp", ".jxl", ".avif" 或 ".json"。

    返回:
    bytes: 图片内容的字节数据。
    """
    # 获取对应状态代码的图片URL
    image_url = get_image_url(service, status_code, image_format)

    # 下载图片并保存在变量中
    image_bytes = download_image(image_url)

    return image_bytes
