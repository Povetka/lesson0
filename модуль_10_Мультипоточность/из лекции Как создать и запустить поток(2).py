# Выполнили задание намного быстрее при помощи потоков.

from threading import Thread
from datetime import datetime
import requests

time_start = datetime.now()

URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
res = []


def collector(url):
    response = requests.get(URL)
    page_response = response.json()
    res.append(page_response)


thr_1 = Thread(target=collector, args=(URL,))
thr_2 = Thread(target=collector, args=(URL,))
thr_3 = Thread(target=collector, args=(URL,))
thr_4 = Thread(target=collector, args=(URL,))
thr_5 = Thread(target=collector, args=(URL,))
thr_6 = Thread(target=collector, args=(URL,))
thr_7 = Thread(target=collector, args=(URL,))
thr_8 = Thread(target=collector, args=(URL,))
thr_9 = Thread(target=collector, args=(URL,))
thr_10 = Thread(target=collector, args=(URL,))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()
thr_5.start()
thr_6.start()
thr_7.start()
thr_8.start()
thr_9.start()
thr_10.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()
thr_5.join()
thr_6.join()
thr_7.join()
thr_8.join()
thr_9.join()
thr_10.join()

time_end = datetime.now()
time_res = time_end - time_start

print(time_res)
print(res)
