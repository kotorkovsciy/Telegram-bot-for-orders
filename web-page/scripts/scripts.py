import random


async def secret_key():
    """Генерация ключа для flask"""
    chars = '+-/*!&$#@?=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    lenght = random.randint(20, 100)
    key = ''
    for i in range(lenght):
        key += random.choice(chars)
    return key
