import random
import os
import datetime

now = datetime.datetime.now()
print(f"Текущее дата и время: {now}")

random = random.randint(1, 10)
print(f"Случайное число: {random}")

files = os.listdir