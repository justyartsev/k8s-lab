import redis

try:
    r = redis.Redis(host='redis', port=6379, decode_responses=True)
    r.ping()
    print(f"Подключено к Redis {'redis'}:{6379}")
except redis.ConnectionError:
    print(f"Ошибка: не удалось подключиться к Redis по адресу {'redis'}:{6379}")

#channel = input("Введите название канала для подписки: ").strip()
#if not channel:
#    print("Название канала не может быть пустым.")
channel = "channel"

pubsub = r.pubsub()
pubsub.subscribe(channel)
print(f"Подписались на канал '{channel}'.(Ctrl+C для выхода)")
'''
try:
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Получено: {message['data']}")
except KeyboardInterrupt:
    print("\nЗавершение работы.")
finally:
    pubsub.unsubscribe()
    r.close()
''' 
for message in pubsub.listen():
    if message['type'] == 'message':
        print(f"Получено: {message['data']}")
#docker-compose up -d redis
#docker-compose run --rm rider