import requests
from bs4 import BeautifulSoup
import os




token = os.getenv("TELEGRAM_BOT_TOKEN")
method_name = "getUpdates"
url = f"https://api.telegram.org/bot{token}/{method_name}"

update = requests.get(url).json()
# print(update)
chat_id = update["result"][0]["message"]["chat"]["id"]
# print(chat_id)
method_name = "sendmessage"

url_kospi = "https://finance.naver.com/sise/"
req_kospi = requests.get(url_kospi).text
soup = BeautifulSoup(req_kospi, 'html.parser')
kospi = soup.select_one("#KOSPI_now")

msg = kospi.text
print(msg)

msg_url = f"https://api.telegram.org/bot{token}/{method_name}?chat_id={chat_id}&text={msg}"


print(msg_url)
print(requests.get(msg_url))