from pathlib import Path
from pprint import pprint
import requests


# парсинг данных статичного сайта (старый форум)
# BASE_URL = "http://forum.rebels-guild.ru/viewtopic.php?f=2&t=6566&start=90"
# BASE_SAVE_PATH = Path("./rebel")
#
# r = requests.get(BASE_URL)
# print(r.status_code)
# html_file_path = BASE_SAVE_PATH / "rebels_forum"
# with open(str(html_file_path.absolute()), "wb") as f:
#     f.write(r.content)
# print("sucsess")

# парсинг текстовых данных
# BASE_URL = "https://jsonplaceholder.typicode.com/posts"
# r = requests.get(BASE_URL)
# parsed_json = r.json()
# pprint(parsed_json[1])

#  парсинг изображений
# BASE_URL = "https://jsonplaceholder.typicode.com/photos"
# r = requests.get(BASE_URL)
# parsed_json = r.json()
# pprint(parsed_json[-1])
# last_img = parsed_json[-1]
# photo_r = requests.get(last_img['url'])
# pprint(photo_r.content)

# парсинг данных GitHub по пользователю
# BASE_URL = 'https://api.github.com/users/Str3et'
# r = requests.get(BASE_URL)
# parsed_json = r.json()
# pprint(parsed_json)

# парсинг hh.ru
BASE_URL = 'https://api.hh.ru/'
vac_r = requests.get(BASE_URL + 'vacancies')
vac_python = requests.get(BASE_URL + 'vacancies/?text=python')
vacancies = vac_r.json()['items']
vacancies_python = vac_python.json()['items']
vac_simple = vac_r.json()['items'][0]
full_vacancies = requests.get('https://api.hh.ru/vacancies/' + vac_simple['id'])
full_vac_py = requests.get('https://api.hh.ru/vacancies/' + vacancies_python[0]['id'])
pprint(full_vac_py.json())

# парсинг данных статичного сайта (старый форум)
# BASE_URL = "http://forum.rebels-guild.ru/viewtopic.php?f=2&t=6566&start=90"

# r = requests.get(BASE_URL)

# soap = BeautifulSoup(r.text, "html.parser")

# print(soap.title)

# msgs = soap.select("div.postbody")

# print(len(msgs))
# print(msgs[-1])

# parsed_msgs = []

# for msg in msgs:
#     txt = msg.get_text()
#     parsed_msgs.append(txt)

# print(len(parsed_msgs))
# print(parsed_msgs[-2])
