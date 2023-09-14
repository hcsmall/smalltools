import requests

# 检测URL是否包含"123"
def check_url_contains_123(url):
    try:
        response = requests.get(url)
        if "123" in response.text:
            return True
    except Exception as e:
        pass
    return False

# 保存包含"123"的URL到ok.txt文件
def save_urls_with_123(urls):
    with open("ok.txt", "w") as file:
        for url in urls:
            file.write(url + "\n")

if __name__ == "__main__":
    # 从文件中读取URL列表，每行一个URL
    with open("urls.txt", "r") as file:
        urls = [line.strip() for line in file]

    urls_with_123 = [url for url in urls if check_url_contains_123(url)]

    if urls_with_123:
        save_urls_with_123(urls_with_123)
        print("包含'123'的URL已保存到ok.txt文件中。")
    else:
        print("未找到包含'123'的URL。")
