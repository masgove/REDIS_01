import redis
client = redis.Redis(host='localhost', port=6379, db=0)

client.set('nome', 'masgove')
print(client.get('nome'))

client.setex('session_id', 30, 'ABCDEF123456')
print(client.ttl('session_id'))
print(client.get('session_id'))
print(client.ttl('session_id'))
print(client.ttl('session_id'))
print(client.get('session_id'))

#client.lpush('animali', 'tigre')
#client.lpush('animali', 'leone','gorilla', 'giraffa')
print('ci sono ', client.llen('animali'), ' animali')
print(client.lindex('animali', 2))
print(client.lpop('animali'))
print(client.lrange('animali', 0, -1))
client.rpush('animali', 'ghepardo')
client.rpush('animali', 'iena')
print(client.lrange('animali', 0, -1))
print(client.rpop('animali'))
print(client.lrange('animali', 0, -1))

pipe=client.pipeline()
pipe.set('numero', 100)
pipe.set('altro_numero', 200)
pipe.get('numero')
print(pipe.execute())

print(client.pipeline().set('citta', 'Milano').set('altra_citta', 'Roma').lpush('nomi', 'Sandro', 'Noemi', 'Elena', 'Ivan').llen('nomi').get('altra_citta').execute())

subscriber = client.pubsub()
subscriber.subscribe('notizie-sport')
subscriber.subscribe('notizie-cinema')

client.publish('notizie-sport', 'Milan-Ascoli 2-1')
client.publish('notizie-sport', 'Roma-Chievo 1-0')

msg=subscriber.get_message()

print(msg)

