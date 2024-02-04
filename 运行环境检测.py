import os
import winreg
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_chrome_version():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Google\Chrome\BLBeacon")
        version, _ = winreg.QueryValueEx(key, "version")
        winreg.CloseKey(key)
        return version
    except FileNotFoundError:
        return None

chromedriver_path = os.path.join(os.getcwd(), 'chromedriver.exe')
if os.path.exists(chromedriver_path):
    chrome_version = get_chrome_version()
    if chrome_version:
        try:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(options=chrome_options)
            # 使用WebDriver访问网页
            driver.get("http://www.baidu.com")  # 将网址替换为你要访问的网页地址
            # 获取网页内容
            page_content = driver.page_source
            # 关闭WebDriver
            driver.quit()
            print(f"chrome浏览器版本：{chrome_version}")
            print("chromedriver.exe与安装的Chrome浏览器匹配")
        except:
            print("chromedriver.exe版本与安装的Chrome浏览器版本不匹配")
    else:
        print("检测未安装Chrome浏览器,请按照最新的chrome浏览器。")
else:
    print("当前目录未发现chromedriver.exe,常用版本下载如下：")
    print("https://googlechromelabs.github.io/chrome-for-testing/#stable")
    print("https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json")
    print("https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/win64/chromedriver-win64.zip")
    print("https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/121.0.6167.85/win64/chromedriver-win64.zip")
input("按任意键继续...")
