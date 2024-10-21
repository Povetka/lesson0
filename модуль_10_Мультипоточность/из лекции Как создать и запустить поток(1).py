# Получаем тз, нужен список из 10 сгенерированных жанров.
# У нас есть страница в интернете, которая генерирует по одному жанру за раз.

import requests
from datetime import datetime

time_start = datetime.now()

URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
res = []

for i in range(10):
    response = requests.get(URL)
    page_response = response.json()
    res.append(page_response)

time_end = datetime.now()
time_res = time_end - time_start

print(time_res)
print(res)

# for genre in res:
#     print(genre)

# Что сделали? Обратились к странице нужное количество раз и собрали все результаты в список.

