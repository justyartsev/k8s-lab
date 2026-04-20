import redis
import time
import logging

r = redis.Redis(host='redis', port=6379, decode_responses=True)
#channel_name = input("Введите название канала: ").strip()
channel_name = "channel"

print(f"Publisher connecting to redis at redis:6379, publishing to '{channel_name}'")

texts = ["Прием","Капучино для Гендальфа","От меня что требуется","Пока"]
'''
while True:
    message = input("Впишите сообщение или выйдете (выход): ").strip()
    if message.lower() == 'выход':
        break
    if message:
        r.publish(channel_name, message)
        print(f"Опубликовано: {message}")
'''

for i in range(len(texts)):
    r.publish(channel_name, texts[i])
    print(f"Опубликовано: {texts[i]}")

    time.sleep(5)
#docker-compose run --rm writer